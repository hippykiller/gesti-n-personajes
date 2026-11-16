from gestor.models.jugador import Estadisticas, Jugador
from gestor.services.gestor_jugadores import GestorJugadores


def _jugador(id_jugador: int = 1) -> Jugador:
    estadisticas = Estadisticas(100, 80, 70, 60, 50)
    return Jugador(
        id_jugador=id_jugador,
        nombre="Julian",
        clase="Guerrero",
        nivel=1,
        estadisticas=estadisticas,
    )


def test_agregar_y_buscar() -> None:
    gestor = GestorJugadores()

    assert gestor.agregar_jugador(_jugador()) is True

    encontrado = gestor.buscar_jugador(1)
    assert encontrado is not None
    assert encontrado.nombre == "Julian"


def test_no_permite_id_duplicado() -> None:
    gestor = GestorJugadores()

    assert gestor.agregar_jugador(_jugador()) is True
    assert gestor.agregar_jugador(_jugador()) is False
    assert len(gestor.jugadores) == 1


def test_modificar_y_eliminar() -> None:
    gestor = GestorJugadores()
    gestor.agregar_jugador(_jugador())

    assert (
        gestor.modificar_jugador(
            1,
            nombre="Borin",
            clase="Mago",
            nivel=5,
            vida=80,
        )
        is True
    )

    jugador = gestor.buscar_jugador(1)
    assert jugador is not None
    assert jugador.nombre == "Borin"
    assert jugador.clase == "Mago"
    assert jugador.nivel == 5
    assert jugador.estadisticas.vida == 80

    assert gestor.eliminar_jugador(1) is True
    assert gestor.buscar_jugador(1) is None
    assert gestor.modificar_jugador(99, nombre="X") is False
