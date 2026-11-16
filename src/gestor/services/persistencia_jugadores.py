"""Carga y guardado de jugadores en la base de datos JSON."""

import json
import unicodedata
from pathlib import Path
from typing import Any

from gestor.models.jugador import Estadisticas, Jugador
from gestor.services.gestor_jugadores import GestorJugadores


def _normalizar(texto: str) -> str:
    """Normaliza nombres de campos para comparar sin acentos."""
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn").lower().strip()


def _obtener_tabla_jugadores(
    datos: list[dict[str, Any]],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Localiza la tabla jugadores y devuelve sus registros."""
    for tabla in datos:
        if tabla.get("type") == "table" and tabla.get("name") == "jugadores":
            filas = tabla.get("data")
            if not isinstance(filas, list):
                raise ValueError("La tabla jugadores no contiene una lista.")
            if not all(isinstance(fila, dict) for fila in filas):
                raise ValueError("Hay registros inválidos en la tabla jugadores.")
            return tabla, filas

    raise ValueError("No se encontró la tabla jugadores en el JSON.")


def _crear_estadisticas(valor: object) -> Estadisticas:
    """Convierte estadísticas antiguas o nuevas al modelo actual."""
    valores = {
        "vida": 100,
        "fuerza": 10,
        "defensa": 10,
        "inteligencia": 10,
        "magia": 10,
    }

    if isinstance(valor, dict):
        for clave, dato in valor.items():
            campo = _normalizar(str(clave))
            if campo in valores:
                valores[campo] = int(dato)

    elif isinstance(valor, str):
        for parte in valor.split(";"):
            if ":" not in parte:
                continue

            clave, dato = parte.split(":", 1)
            campo = _normalizar(clave)

            if campo in valores:
                valores[campo] = int(dato.strip())

    return Estadisticas(**valores)


def cargar_gestor_desde_json(
    ruta_archivo: Path,
) -> tuple[list[dict[str, Any]], GestorJugadores]:
    """Carga jugadores del JSON y los convierte en objetos."""
    with ruta_archivo.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError("La raíz del archivo JSON debe ser una lista.")

    tabla, filas = _obtener_tabla_jugadores(datos)
    gestor = GestorJugadores()

    for numero, fila in enumerate(filas, start=1):
        try:
            estadisticas = _crear_estadisticas(
                fila.get("Estadísticas", fila.get("estadisticas"))
            )

            jugador = Jugador(
                id_jugador=int(fila["id_jugador"]),
                nombre=str(fila.get("Nombre") or fila.get("nombre") or "Sin Nombre"),
                clase=str(fila.get("Clase") or fila.get("clase") or "Aventurero"),
                nivel=int(fila.get("Nivel") or fila.get("nivel") or 1),
                estadisticas=estadisticas,
            )

            if not gestor.agregar_jugador(jugador):
                raise ValueError("Hay un ID de jugador duplicado.")

        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                f"Error al cargar el registro {numero} de jugadores: {error}"
            ) from error

    return datos, gestor


def _serializar_estadisticas(
    jugador: Jugador, registro_original: dict[str, Any]
) -> str:
    """Serializa las cinco estadísticas y conserva campos antiguos desconocidos."""
    extras: list[str] = []
    original = registro_original.get(
        "Estadísticas",
        registro_original.get("estadisticas", ""),
    )

    campos_conocidos = {
        "vida",
        "fuerza",
        "defensa",
        "inteligencia",
        "magia",
    }

    if isinstance(original, str):
        for parte in original.split(";"):
            if ":" not in parte:
                continue

            clave, valor = parte.split(":", 1)
            if _normalizar(clave) not in campos_conocidos:
                extras.append(f"{clave.strip()}: {valor.strip()}")

    stats = jugador.estadisticas

    partes = [
        f"Vida: {stats.vida}",
        f"Fuerza: {stats.fuerza}",
        f"Defensa: {stats.defensa}",
        f"Inteligencia: {stats.inteligencia}",
        f"Magia: {stats.magia}",
    ]

    return " ; ".join(partes + extras)


def guardar_gestor_en_json(
    ruta_archivo: Path,
    datos: list[dict[str, Any]],
    gestor: GestorJugadores,
) -> None:
    """Actualiza jugadores sin modificar las tablas items e inventario."""
    tabla, filas_originales = _obtener_tabla_jugadores(datos)

    originales_por_id = {str(fila.get("id_jugador")): fila for fila in filas_originales}

    nuevos_registros: list[dict[str, Any]] = []

    for jugador in gestor.jugadores:
        original = originales_por_id.get(str(jugador.id_jugador), {})
        registro = dict(original)

        registro.update(
            {
                "id_jugador": str(jugador.id_jugador),
                "Nombre": jugador.nombre,
                "Clase": jugador.clase,
                "Nivel": str(jugador.nivel),
                "Estadísticas": _serializar_estadisticas(jugador, original),
            }
        )

        nuevos_registros.append(registro)

    tabla["data"] = nuevos_registros

    temporal = ruta_archivo.with_suffix(ruta_archivo.suffix + ".tmp")

    try:
        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        temporal.replace(ruta_archivo)

    except OSError:
        if temporal.exists():
            temporal.unlink()
        raise
