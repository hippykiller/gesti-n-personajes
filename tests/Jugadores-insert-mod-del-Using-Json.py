# AUTOR-- Brasesco Malara Tomás David
import json
import sys
from pathlib import Path

from src.gestor.models.jugador import Estadisticas, Jugador
from src.gestor.services.gestor_jugadores import GestorJugadores

# 1. RUTA DEL ARCHIVO
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.append(str(RAIZ_PROYECTO))

archivo_json = RAIZ_PROYECTO / "data" / "bd_unab_grupo6.json"


# 2. FUNCIONES DE CONVERSIÓN (JSON <-> OBJETOS)
def obtener_tabla_jugadores(datos):
    for tabla in datos:
        if tabla.get("name") == "jugadores":
            return tabla["data"]
    return None


def cargar_gestor_desde_json(ruta_archivo):
    """Lee el JSON y llena un objeto GestorJugadores con instancias de Jugador."""
    with open(ruta_archivo, encoding="utf-8") as f:
        datos = json.load(f)

    gestor = GestorJugadores()
    lista_cruda = obtener_tabla_jugadores(datos)

    if lista_cruda:
        for item in lista_cruda:
            # Extraemos o adaptamos las estadísticas
            est_data = item.get("estadisticas")
            if isinstance(est_data, dict):
                stats = Estadisticas(
                    vida=int(est_data.get("vida", 100)),
                    fuerza=int(est_data.get("fuerza", 10)),
                    defensa=int(est_data.get("defensa", 10)),
                    inteligencia=int(est_data.get("inteligencia", 10)),
                    magia=int(est_data.get("magia", 10)),
                )
            else:
                # Si es un registro viejo del JSON de phpMyAdmin, ponemos valores base
                stats = Estadisticas(100, 10, 10, 10, 10)

            jugador = Jugador(
                id_jugador=int(item["id_jugador"]),
                nombre=item.get("nombre") or item.get("Nombre", "Sin Nombre"),
                clase=item.get("clase", "Aventurero"),
                nivel=int(item.get("nivel") or item.get("Nivel", 1)),
                estadisticas=stats,
            )
            gestor.agregar_jugador(jugador)

    return datos, gestor


def guardar_gestor_en_json(ruta_archivo, datos, gestor):
    """Convierte los objetos del GestorJugadores a diccionarios y actualiza el JSON."""
    lista_serializada = []

    for j in gestor.jugadores:
        lista_serializada.append(
            {
                "id_jugador": str(j.id_jugador),
                "nombre": j.nombre,
                "clase": j.clase,
                "nivel": str(j.nivel),
                "estadisticas": {
                    "vida": j.estadisticas.vida,
                    "fuerza": j.estadisticas.fuerza,
                    "defensa": j.estadisticas.defensa,
                    "inteligencia": j.estadisticas.inteligencia,
                    "magia": j.estadisticas.magia,
                },
            }
        )

    # Reemplazamos la lista 'data' dentro de la tabla 'jugadores'
    for tabla in datos:
        if tabla.get("name") == "jugadores":
            tabla["data"] = lista_serializada
            break

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


# 3. FUNCIONES DE ALTA, BAJA Y MODIFICACIÓN USANDO TUS CLASES
def dar_alta_jugador(datos, gestor):
    print("\n--- Alta de Nuevo Jugador ---")
    try:
        id_j = int(input("ID del jugador (entero >= 1): "))
        if gestor.buscar_jugador(id_j) is not None:
            print(f"[!] Error: Ya existe un jugador con ID {id_j}.")
            return

        nombre = input("Nombre: ")
        clase = input("Clase (ej. Guerrero, Mago): ")
        nivel = int(input("Nivel (1-100): "))

        print("Ingresa las estadísticas (0-100):")
        vida = int(input("  Vida: "))
        fuerza = int(input("  Fuerza: "))
        defensa = int(input("  Defensa: "))
        inteligencia = int(input("  Inteligencia: "))
        magia = int(input("  Magia: "))

        # Tus clases validan automáticamente todos los rangos y tipos aquí
        stats = Estadisticas(vida, fuerza, defensa, inteligencia, magia)
        nuevo_jugador = Jugador(id_j, nombre, clase, nivel, stats)

        gestor.agregar_jugador(nuevo_jugador)
        guardar_gestor_en_json(archivo_json, datos, gestor)
        print(f"¡Jugador '{nuevo_jugador.nombre}' guardado con éxito!")

    except ValueError as e:
        # Captura tanto errores de int() como los raise ValueError de tus setters
        print(f"[!] Dato inválido: {e}")


def modificar_jugador_menu(datos, gestor):
    print("\n--- Modificar Jugador ---")
    try:
        id_j = int(input("ID del jugador a modificar: "))
        if gestor.buscar_jugador(id_j) is None:
            print(f"[!] No existe un jugador con ID {id_j}.")
            return

        print("(Presiona Enter sin escribir nada para mantener el valor actual)")
        nombre = input("Nuevo nombre: ").strip() or None
        clase = input("Nueva clase: ").strip() or None

        nivel_str = input("Nuevo nivel (1-100): ").strip()
        nivel = int(nivel_str) if nivel_str else None

        vida_str = input("Nueva vida (0-100): ").strip()
        vida = int(vida_str) if vida_str else None

        fuerza_str = input("Nueva fuerza (0-100): ").strip()
        fuerza = int(fuerza_str) if fuerza_str else None

        defensa_str = input("Nueva defensa (0-100): ").strip()
        defensa = int(defensa_str) if defensa_str else None

        int_str = input("Nueva inteligencia (0-100): ").strip()
        inteligencia = int(int_str) if int_str else None

        magia_str = input("Nueva magia (0-100): ").strip()
        magia = int(magia_str) if magia_str else None

        # Usamos el método de tu GestorJugadores (que dispara tus setters)
        exito = gestor.modificar_jugador(
            id_j, nombre, clase, nivel, vida, fuerza, defensa, inteligencia, magia
        )

        if exito:
            guardar_gestor_en_json(archivo_json, datos, gestor)
            print("¡Jugador modificado y guardado en el JSON!")

    except ValueError as e:
        print(f"[!] Error al modificar: {e}")


def dar_baja_jugador(datos, gestor):
    print("\n--- Baja de Jugador ---")
    try:
        id_j = int(input("ID del jugador a eliminar: "))
        if gestor.eliminar_jugador(id_j):
            guardar_gestor_en_json(archivo_json, datos, gestor)
            print(f"¡Jugador con ID {id_j} eliminado correctamente!")
        else:
            print(f"[!] No se encontró un jugador con ID {id_j}.")
    except ValueError:
        print("[!] El ID debe ser un número entero.")
