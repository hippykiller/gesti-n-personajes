"""
Módulo: app.py
Descripción: Controlador principal de navegación y flujo
de la aplicación de consola para el sistema de gestión.
"""

from collections.abc import Callable

from gestor.models.jugador import Jugador
from gestor.services.gestor_jugadores import GestorJugadores
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
from gestor.validaciones import pedir_entero_positivo, pedir_texto

gestor_jugadores = GestorJugadores()


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


def _crear_jugador() -> None:
    """Pide los datos y crea una cuenta de jugador."""
    id_jugador = pedir_entero_positivo("ID del jugador: ")
    nombre_user = pedir_texto("Nombre de usuario: ")
    personaje = pedir_texto("Personaje elegido: ")
    id_inventario = pedir_entero_positivo("ID de inventario: ")
    jugador = Jugador(
        id_jugador=id_jugador,
        nombre_user=nombre_user,
        contrasena_hash="sin_definir",
        personaje_elegido=personaje,
        id_inventario=id_inventario,
    )
    if gestor_jugadores.agregar_jugador(jugador):
        print("\nJugador creado correctamente.")
    else:
        print("\nError: ya existe un jugador con ese ID.")
    input("Presione ENTER para continuar...")


def _buscar_jugador() -> None:
    """Busca un jugador por ID y muestra sus datos (sin la contraseña)."""
    id_jugador = pedir_entero_positivo("ID a buscar: ")
    jugador = gestor_jugadores.buscar_jugador(id_jugador)
    if jugador is None:
        print("\nNo se encontró el jugador.")
    else:
        activo = "activa" if jugador.estado_cuenta else "inactiva"
        print(f"\nID: {jugador.id_jugador}")
        print(f"Usuario: {jugador.nombre_user}")
        print(f"Personaje: {jugador.personaje_elegido}")
        print(f"Inventario: {jugador.id_inventario}")
        print(f"Cuenta: {activo}")
    input("Presione ENTER para continuar...")


def sub_menu_jugadores() -> None:
    """Muestra el submenú de jugadores y gestiona su navegación."""
    while True:
        limpiar_pantalla()
        mostrar_menu_jugadores()
        opcion = leer_opcion("\nSeleccioná una opción: ", (0, 1, 2))
        if opcion == 0:
            return
        elif opcion == 1:
            _crear_jugador()
        elif opcion == 2:
            _buscar_jugador()


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
