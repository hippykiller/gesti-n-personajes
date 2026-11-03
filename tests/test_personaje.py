import pytest

from gestor.models.personaje import ClasePersonaje, Personaje


@pytest.fixture
def guerrero() -> Personaje:
    return Personaje(id_personaje=1, nombre="Thor", clase=ClasePersonaje.GUERRERO)


def test_valores_por_defecto(guerrero: Personaje) -> None:
    assert guerrero.nivel == 1
    assert guerrero.vida == 100
    assert guerrero.ataque == 10
    assert guerrero.defensa == 5
    assert guerrero.clase is ClasePersonaje.GUERRERO


def test_el_nombre_se_limpia_de_espacios() -> None:
    personaje = Personaje(1, "  Merlin  ", ClasePersonaje.MAGO)
    assert personaje.nombre == "Merlin"


@pytest.mark.parametrize("nombre_invalido", ["", "   "])
def test_nombre_vacio_da_error(nombre_invalido: str) -> None:
    with pytest.raises(ValueError, match="nombre"):
        Personaje(1, nombre_invalido, ClasePersonaje.ARQUERO)


def test_nivel_menor_a_uno_da_error() -> None:
    with pytest.raises(ValueError, match="nivel"):
        Personaje(1, "Legolas", ClasePersonaje.ARQUERO, nivel=0)


@pytest.mark.parametrize("campo", ["vida", "ataque", "defensa"])
def test_atributos_negativos_dan_error(campo: str) -> None:
    with pytest.raises(ValueError, match=campo):
        Personaje(1, "Legolas", ClasePersonaje.ARQUERO, **{campo: -1})


def test_recibir_dano_resta_vida(guerrero: Personaje) -> None:
    guerrero.recibir_dano(30)
    assert guerrero.vida == 70
    assert guerrero.esta_vivo()


def test_la_vida_nunca_baja_de_cero(guerrero: Personaje) -> None:
    guerrero.recibir_dano(500)
    assert guerrero.vida == 0
    assert not guerrero.esta_vivo()


def test_dano_negativo_da_error(guerrero: Personaje) -> None:
    with pytest.raises(ValueError, match="daño"):
        guerrero.recibir_dano(-5)


def test_subir_nivel(guerrero: Personaje) -> None:
    guerrero.subir_nivel()
    assert guerrero.nivel == 2
