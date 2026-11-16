from gestor.services.data_loader import cargar_base_datos, obtener_tabla


def test_cargar_base_datos() -> None:
    datos = cargar_base_datos()
    assert isinstance(datos, list)


def test_obtener_tabla_jugadores() -> None:
    jugadores = obtener_tabla("jugadores")
    assert len(jugadores) >= 1
    assert "id_jugador" in jugadores[0]
