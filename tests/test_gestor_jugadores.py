from gestor.models.jugador import Jugador
from gestor.services.gestor_jugadores import GestorJugadores


def _jugador(id_jugador: int = 1) -> Jugador:
    return Jugador(
        id_jugador=id_jugador,
        nombre_user="JulianP",
        contrasena_hash="fake_hash",
        personaje_elegido="Guerrero",
        id_inventario=100,
    )


def test_agregar_y_buscar() -> None:
    gestor = GestorJugadores()
    assert gestor.agregar_jugador(_jugador()) is True
    encontrado = gestor.buscar_jugador(1)
    assert encontrado is not None
    assert encontrado.nombre_user == "JulianP"


def test_no_permite_id_duplicado() -> None:
    gestor = GestorJugadores()
    gestor.agregar_jugador(_jugador())
    assert gestor.agregar_jugador(_jugador()) is False
    assert len(gestor.jugadores) == 1


def test_modificar_y_eliminar() -> None:
    gestor = GestorJugadores()
    gestor.agregar_jugador(_jugador())
    assert gestor.modificar_jugador(1, estado_cuenta=False) is True
    jugador = gestor.buscar_jugador(1)
    assert jugador is not None
    assert jugador.estado_cuenta is False
    assert gestor.eliminar_jugador(1) is True
    assert gestor.buscar_jugador(1) is None
    assert gestor.modificar_jugador(99, nombre_user="X") is False
