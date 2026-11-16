"""
Módulo: menu.py
Descripción: Funciones de presentación y utilidades de consola para renderizar los menús y validar las entradas.
"""

import os


def limpiar_pantalla() -> None:
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def leer_opcion(mensaje: str, opciones_validas: tuple[int, ...]) -> int:
    """
    Solicita una opción por consola y valida que sea un entero dentro de las opciones permitidas.
    """
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            print(
                f" Error: Opción no válida. Elija una de las siguientes: {opciones_validas}"
            )
        except ValueError:
            print(" Error: Debe ingresar un número entero.")


def mostrar_encabezado(titulo: str) -> None:
    """Imprime un encabezado con formato en la consola."""
    print("\n" + "=" * 40)
    print(f" {titulo}")
    print("=" * 40)


def mostrar_menu_principal() -> None:
    """Muestra las opciones del menú principal del sistema."""
    mostrar_encabezado("SISTEMA DE GESTIÓN - MENÚ PRINCIPAL")
    print("1. Gestión de Jugadores")
    print("2. Gestión de Personajes")
    print("3. Gestión de Ítems")
    print("4. Gestión de Inventarios")
    print("5. Consultas")
    print("0. Salir")


def mostrar_menu_jugadores() -> None:
    """Muestra las opciones del submenú de jugadores."""
    mostrar_encabezado("GESTIÓN DE JUGADORES")
    print("1. Crear Jugador")
    print("2. Buscar Jugador")
    print("0. Regresar al Menú Principal")


def mostrar_menu_personajes() -> None:
    """Muestra las opciones del submenú de personajes."""
    mostrar_encabezado("GESTIÓN DE PERSONAJES")
    print("1. Crear Personaje")
    print("2. Buscar Personaje")
    print("0. Regresar al Menú Principal")


def mostrar_menu_items() -> None:
    """Muestra las opciones del submenú de ítems."""
    mostrar_encabezado("GESTIÓN DE ÍTEMS")
    print("1. Registrar Ítem")
    print("2. Buscar Ítem")
    print("0. Regresar al Menú Principal")


def mostrar_menu_inventarios() -> None:
    """Muestra las opciones del submenú de inventarios."""
    mostrar_encabezado("GESTIÓN DE INVENTARIOS")
    print("1. Asignar Ítem a un Personaje")
    print("2. Consultar Inventario")
    print("0. Regresar al Menú Principal")


def mostrar_menu_consultas() -> None:
    """Muestra las opciones del submenú de consultas."""
    mostrar_encabezado("CONSULTAS")
    print("1. Consultar Personajes")
    print("2. Consultar Inventarios")
    print("0. Regresar al Menú Principal")
