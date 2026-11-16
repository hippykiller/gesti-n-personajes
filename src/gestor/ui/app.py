"""
Módulo: app.py
Descripción: Controlador principal de navegación y flujo
de la aplicación de consola para el sistema de gestión.
"""

from collections.abc import Callable
from pathlib import Path

from gestor.services.persistencia_jugadores import (
    cargar_gestor_desde_json,
    guardar_gestor_en_json,
)
from gestor.ui.menu import (
    leer_opcion,
    limpiar_pantalla,
    mostrar_menu_consultas,
    mostrar_menu_inventarios,
    mostrar_menu_items,
    mostrar_menu_personajes,
    mostrar_menu_principal,
)
from gestor.ui.pantallas.jugadores import menu_jugadores

# Ruta absoluta al archivo JSON del proyecto.
RUTA_JSON = Path(__file__).resolve().parents[3] / "data" / "bd_unab_grupo6.json"

# Cargar los datos y crear el gestor con los jugadores existentes.
datos_json, gestor_jugadores = cargar_gestor_desde_json(RUTA_JSON)


def guardar_jugadores() -> None:
    """Guarda los jugadores en el archivo JSON."""
    guardar_gestor_en_json(RUTA_JSON, datos_json, gestor_jugadores)


def _mostrar_modulo_en_desarrollo() -> None:
    """Muestra un mensaje temporal para operaciones aún no implementadas."""
    print("\n[INFO] Este módulo o funcionalidad se encuentra en desarrollo.")
    input("Presione ENTER para continuar...")


def _ejecutar_submenu(
    mostrar_menu_fn: Callable[[], None],
    opciones_validas: tuple[int, ...],
) -> None:
    """Controla la navegación de los submenús todavía no implementados."""
    while True:
        limpiar_pantalla()
        mostrar_menu_fn()
        opcion = leer_opcion("\nSeleccioná una opción: ", opciones_validas)

        if opcion == 0:
            return

        _mostrar_modulo_en_desarrollo()


def sub_menu_jugadores() -> None:
    """Muestra el submenú de jugadores y guarda los cambios al salir."""
    menu_jugadores(gestor_jugadores)
    guardar_jugadores()


def sub_menu_personajes() -> None:
    """Muestra el submenú de personajes."""
    _ejecutar_submenu(mostrar_menu_personajes, (0, 1, 2))


def sub_menu_items() -> None:
    """Muestra el submenú de ítems."""
    _ejecutar_submenu(mostrar_menu_items, (0, 1, 2))


def sub_menu_inventarios() -> None:
    """Muestra el submenú de inventarios."""
    _ejecutar_submenu(mostrar_menu_inventarios, (0, 1, 2))


def sub_menu_consultas() -> None:
    """Muestra el submenú de consultas."""
    _ejecutar_submenu(mostrar_menu_consultas, (0, 1, 2))


def ejecutar_app() -> None:
    """Ejecuta el menú principal hasta que el usuario elija salir."""
    opciones_principales = (0, 1, 2, 3, 4, 5)

    while True:
        limpiar_pantalla()
        mostrar_menu_principal()

        opcion = leer_opcion(
            "\nSeleccioná una opción: ",
            opciones_principales,
        )

        if opcion == 0:
            guardar_jugadores()
            print("\nGracias por utilizar el sistema. ¡Hasta pronto!")
            break

        elif opcion == 1:
            sub_menu_jugadores()

        elif opcion == 2:
            sub_menu_personajes()

        elif opcion == 3:
            sub_menu_items()

        elif opcion == 4:
            sub_menu_inventarios()

        elif opcion == 5:
            sub_menu_consultas()


if __name__ == "__main__":
    ejecutar_app()
