"""Pantalla de gestión de jugadores: registrar, buscar por ID y listar."""

from gestor.models.jugador import Estadisticas, Jugador
from gestor.services.gestor_jugadores import GestorJugadores
from gestor.ui.menu import limpiar_pantalla, mostrar_encabezado
from gestor.validaciones import pedir_entero, pedir_texto


def _registrar(gestor: GestorJugadores) -> None:
    mostrar_encabezado("REGISTRAR JUGADOR")
    id_jugador = pedir_entero("ID del jugador: ", minimo=1)

    if gestor.buscar_jugador(id_jugador) is not None:
        print("\nError: ya existe un jugador registrado con ese ID.")
        return

    nombre = pedir_texto("Nombre del jugador: ")
    clase = pedir_texto("Clase (ej. Guerrero, Mago): ")
    nivel = pedir_entero("Nivel inicial (1 a 100): ", minimo=1, maximo=100)

    print("\n--- Carga de Estadísticas Iniciales ---")
    vida = pedir_entero("Vida (0 a 100): ", minimo=0, maximo=100)
    fuerza = pedir_entero("Fuerza (0 a 100): ", minimo=0, maximo=100)
    defensa = pedir_entero("Defensa (0 a 100): ", minimo=0, maximo=100)
    inteligencia = pedir_entero("Inteligencia (0 a 100): ", minimo=0, maximo=100)
    magia = pedir_entero("Magia (0 a 100): ", minimo=0, maximo=100)

    stats = Estadisticas(
        vida=vida,
        fuerza=fuerza,
        defensa=defensa,
        inteligencia=inteligencia,
        magia=magia,
    )

    jugador = Jugador(
        id_jugador=id_jugador,
        nombre=nombre,
        clase=clase,
        nivel=nivel,
        estadisticas=stats,
    )

    gestor.agregar_jugador(jugador)
    print(f"\n¡Jugador '{nombre}' registrado con éxito!")


def _buscar(gestor: GestorJugadores) -> None:
    mostrar_encabezado("BUSCAR JUGADOR POR ID")
    id_jugador = pedir_entero("ID a buscar: ", minimo=1)
    jugador = gestor.buscar_jugador(id_jugador)

    if jugador is None:
        print("\nNo se encontró ningún jugador con ese ID.")
        return

    print(f"\nID: {jugador.id_jugador}")
    print(f"Nombre: {jugador.nombre}")
    print(f"Clase: {jugador.clase}")
    print(f"Nivel: {jugador.nivel}")
    print("Estadísticas:")
    print(f"  - Vida: {jugador.estadisticas.vida}")
    print(f"  - Fuerza: {jugador.estadisticas.fuerza}")
    print(f"  - Defensa: {jugador.estadisticas.defensa}")
    print(f"  - Inteligencia: {jugador.estadisticas.inteligencia}")
    print(f"  - Magia: {jugador.estadisticas.magia}")


def _listar(gestor: GestorJugadores) -> None:
    mostrar_encabezado("LISTA DE JUGADORES REGISTRADOS")
    if not gestor.jugadores:
        print("No hay jugadores cargados en la memoria.")
        return

    print(f"{'ID':<5}{'Nombre':<20}{'Clase':<15}{'Nivel':<7}")
    print("-" * 47)
    for jugador in sorted(gestor.jugadores, key=lambda j: j.id_jugador):
        print(
            f"{jugador.id_jugador:<5}{jugador.nombre:<20}"
            f"{jugador.clase:<15}{jugador.nivel:<7}"
        )


def menu_jugadores(gestor: GestorJugadores) -> None:
    """Submenú de jugadores. La opción 0 regresa al menú principal."""
    while True:
        limpiar_pantalla()
        mostrar_encabezado("GESTIÓN DE JUGADORES")
        print("1. Registrar Jugador")
        print("2. Buscar Jugador por ID")
        print("3. Listar Todos los Jugadores")
        print("0. Regresar al Menú Principal")

        opcion = pedir_entero("\nSeleccioná una opción: ", minimo=0, maximo=3)

        if opcion == 0:
            return
        elif opcion == 1:
            _registrar(gestor)
        elif opcion == 2:
            _buscar(gestor)
        elif opcion == 3:
            _listar(gestor)

        input("\nPresione ENTER para continuar...")


# Alias para garantizar compatibilidad con invocaciones en app.py
sub_menu_jugadores = menu_jugadores
