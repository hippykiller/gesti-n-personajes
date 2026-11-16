"""
Módulo: app.py
Descripción: Controlador principal de navegación y flujo
de la aplicación de consola para el sistema de gestión.
"""

from collections.abc import Callable

# Importación de las funciones de pantalla y utilidades desde menu.py
from gestor.ui.menu import (
    leer_opcion,
    limpiar_pantalla,
    mostrar_menu_consultas,
    mostrar_menu_inventarios,
    mostrar_menu_items,
    mostrar_menu_jugadores,
    mostrar_menu_personajes,
    mostrar_menu_principal,
)


def _mostrar_modulo_en_desarrollo() -> None:
    """Muestra un mensaje temporal para operaciones aún no implementadas."""
    print("\n[INFO] Este módulo o funcionalidad se encuentra en desarrollo.")
    input("Presione ENTER para continuar...")


def _ejecutar_submenu(
    mostrar_menu_fn: Callable[[], None], opciones_validas: tuple[int, ...]
) -> None:
    """
    Función auxiliar genérica para controlar la navegación de cualquier submenú.
    Recibe la función que dibuja el submenú y la tupla con sus opciones válidas.
    """
    while True:
        limpiar_pantalla()
        mostrar_menu_fn()
        opcion = leer_opcion("\nSeleccioná una opción: ", opciones_validas)
        if opcion == 0:
            return  # Finaliza el submenú y regresa al menú anterior
        _mostrar_modulo_en_desarrollo()


def sub_menu_jugadores() -> None:
    """Muestra el submenú de jugadores y gestiona su navegación."""
    _ejecutar_submenu(mostrar_menu_jugadores, (0, 1, 2))


def sub_menu_personajes() -> None:
    """Muestra el submenú de personajes y gestiona su navegación."""
    _ejecutar_submenu(mostrar_menu_personajes, (0, 1, 2))


def sub_menu_items() -> None:
    """Muestra el submenú de ítems y gestiona su navegación."""
    _ejecutar_submenu(mostrar_menu_items, (0, 1, 2))


def sub_menu_inventarios() -> None:
    """Muestra el submenú de inventarios y gestiona su navegación."""
    _ejecutar_submenu(mostrar_menu_inventarios, (0, 1, 2))


def sub_menu_consultas() -> None:
    """Muestra el submenú de consultas y gestiona su navegación."""
    _ejecutar_submenu(mostrar_menu_consultas, (0, 1, 2))


def ejecutar_app() -> None:
    """Ejecuta el menú principal en bucle hasta que el usuario elija Salir."""
    opciones_principales = (0, 1, 2, 3, 4, 5)
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = leer_opcion("\nSeleccioná una opción: ", opciones_principales)
        if opcion == 0:
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
