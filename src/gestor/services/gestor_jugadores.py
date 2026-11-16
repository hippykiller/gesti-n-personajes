"""Gestión en memoria de los jugadores."""

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
        """Devuelve el jugador encontrado o None."""
        for jugador in self.jugadores:
            if jugador.id_jugador == id_jugador:
                return jugador
        return None

    def modificar_jugador(
        self,
        id_jugador: int,
        nombre: str | None = None,
        clase: str | None = None,
        nivel: int | None = None,
        vida: int | None = None,
        fuerza: int | None = None,
        defensa: int | None = None,
        inteligencia: int | None = None,
        magia: int | None = None,
    ) -> bool:
        """Modifica los campos indicados. Devuelve False si no existe."""
        jugador = self.buscar_jugador(id_jugador)

        if jugador is None:
            return False

        if nombre is not None:
            jugador.nombre = nombre
        if clase is not None:
            jugador.clase = clase
        if nivel is not None:
            jugador.nivel = nivel
        if vida is not None:
            jugador.estadisticas.vida = vida
        if fuerza is not None:
            jugador.estadisticas.fuerza = fuerza
        if defensa is not None:
            jugador.estadisticas.defensa = defensa
        if inteligencia is not None:
            jugador.estadisticas.inteligencia = inteligencia
        if magia is not None:
            jugador.estadisticas.magia = magia

        return True

    def eliminar_jugador(self, id_jugador: int) -> bool:
        """Elimina el jugador. Devuelve False si no existe."""
        jugador = self.buscar_jugador(id_jugador)

        if jugador is None:
            return False

        self.jugadores.remove(jugador)
        return True
