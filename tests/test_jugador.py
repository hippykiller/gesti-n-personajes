from src.gestor.models.jugador import Jugador


def test_creacion_jugador():
    # Creamos un jugador de prueba con el molde
    jugador1 = Jugador(
        id_jugador=1,
        nombre_user="JulianP",
        contrasena_hash="fake_hash_123",
        personaje_elegido="Guerrero",
        id_inventario=100,
    )

    # Verificamos que los datos se guarden bien y el default funcione
    assert jugador1.nombre_user == "JulianP"
    assert jugador1.personaje_elegido == "Guerrero"
    assert jugador1.estado_cuenta is True  # Arranca activo por defecto


def test_se_puede_crear_cuenta_inactiva():
    # Probamos el caso donde la cuenta se crea dada de baja a propósito
    baja = Jugador(
        id_jugador=2,
        nombre_user="Borin",
        contrasena_hash="hash_falso",
        personaje_elegido="Guerrero",
        id_inventario=101,
        estado_cuenta=False,
    )
    assert baja.estado_cuenta is False
    assert baja.nombre_user == "Borin"
