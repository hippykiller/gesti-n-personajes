import json
from pathlib import Path
from typing import Any


def cargar_base_datos() -> list[dict[str, Any]]:
    """Lee el export JSON de phpMyAdmin con la base de datos del grupo."""
    ruta_raiz = Path(__file__).resolve().parents[3]
    ruta_archivo = ruta_raiz / "data" / "bd_unab_grupo6.json"

    with open(ruta_archivo, encoding="utf-8") as archivo:
        datos: list[dict[str, Any]] = json.load(archivo)
    return datos


def obtener_tabla(nombre: str) -> list[dict[str, Any]]:
    """Devuelve las filas de una tabla del export (por ejemplo 'jugadores')."""
    for bloque in cargar_base_datos():
        if bloque.get("type") == "table" and bloque.get("name") == nombre:
            filas: list[dict[str, Any]] = bloque["data"]
            return filas
    return []
