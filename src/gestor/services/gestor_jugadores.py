from src.gestor.models.jugador import Jugador


class GestorJugadores:

    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def buscar_jugador(self, id_jugador):
        for jugador in self.jugadores:
            if jugador.id_jugador == id_jugador:
                return jugador

        return None
    
    def modificar_jugador(self, id_jugador, nombre=None, clase=None, nivel=None,
                    vida=None, fuerza=None, defensa=None,
                    inteligencia=None, magia=None):

        jugador = self.buscar_jugador(id_jugador)

        if jugador is not None:
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

        return False


    def eliminar_jugador(self, id_jugador):
        jugador = self.buscar_jugador(id_jugador)

        if jugador is not None:
            self.jugadores.remove(jugador)
            return True

        return False
