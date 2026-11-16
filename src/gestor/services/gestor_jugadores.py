"""Gestión en memoria de las cuentas de jugadores."""

from gestor.models.jugador import Jugador


class GestorJugadores:
    """Agrega, busca, modifica y elimina jugadores."""

    def __init__(self) -> None:
        self.jugadores: list[Jugador] = []

    def agregar_jugador(self, jugador: Jugador) -> bool:
        """Agrega el jugador. Devuelve False si el ID ya existe."""
        if self.buscar_jugador(jugador.id_jugador) is not None:
            return False
        self.jugadores.append(jugador)
        return True

    def buscar_jugador(self, id_jugador: int) -> Jugador | None:
        """Devuelve el jugador con ese ID, o None si no existe."""
        for jugador in self.jugadores:
            if jugador.id_jugador == id_jugador:
                return jugador
        return None

    def modificar_jugador(
        self,
        id_jugador: int,
        nombre_user: str | None = None,
        personaje_elegido: str | None = None,
        estado_cuenta: bool | None = None,
    ) -> bool:
        """Modifica los campos indicados. Devuelve False si no existe."""
        jugador = self.buscar_jugador(id_jugador)
        if jugador is None:
            return False
        if nombre_user is not None:
            jugador.nombre_user = nombre_user
        if personaje_elegido is not None:
            jugador.personaje_elegido = personaje_elegido
        if estado_cuenta is not None:
            jugador.estado_cuenta = estado_cuenta
        return True

    def eliminar_jugador(self, id_jugador: int) -> bool:
        """Elimina el jugador. Devuelve False si no existe."""
        jugador = self.buscar_jugador(id_jugador)
        if jugador is None:
            return False
        self.jugadores.remove(jugador)
        return True
