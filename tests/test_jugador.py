import pytest

from gestor.models.jugador import Estadisticas, Jugador


def _jugador() -> Jugador:
    estadisticas = Estadisticas(
        vida=100,
        fuerza=80,
        defensa=70,
        inteligencia=60,
        magia=50,
    )
    return Jugador(
        id_jugador=1,
        nombre="Julian",
        clase="Guerrero",
        nivel=1,
        estadisticas=estadisticas,
    )


def test_creacion_jugador() -> None:
    jugador = _jugador()

    assert jugador.id_jugador == 1
    assert jugador.nombre == "Julian"
    assert jugador.clase == "Guerrero"
    assert jugador.nivel == 1
    assert jugador.estadisticas.vida == 100


def test_validacion_estadisticas() -> None:
    with pytest.raises(ValueError):
        Estadisticas(vida=101, fuerza=50, defensa=50, inteligencia=50, magia=50)


def test_validacion_nivel() -> None:
    with pytest.raises(ValueError):
        Jugador(
            id_jugador=1,
            nombre="Julian",
            clase="Guerrero",
            nivel=101,
            estadisticas=Estadisticas(100, 80, 70, 60, 50),
        )
