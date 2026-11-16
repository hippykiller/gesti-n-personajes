"""Punto de entrada del programa."""

import sys
from pathlib import Path

# Agregar la carpeta src a la ruta de búsqueda de Python.
RUTA_SRC = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(RUTA_SRC))

from gestor.ui.app import ejecutar_app  # noqa: E402

if __name__ == "__main__":
    ejecutar_app()
