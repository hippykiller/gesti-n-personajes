import json
from pathlib import Path
from typing import Any, Dict

def cargar_base_datos() -> Dict[str, Any]:
    """Lee el archivo JSON de la base de datos del grupo de forma robusta."""
    # Obtenemos la raíz del proyecto de forma dinámica usando la ubicación de este archivo
    ruta_raiz = Path(__file__).resolve().parents[3]
    ruta_archivo = ruta_raiz / "data" / "bd_unab_grupo6.json"

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos: Dict[str, Any] = json.load(archivo)
        return datos