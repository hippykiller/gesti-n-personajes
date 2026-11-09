
from src.gestor.models.jugador import Estadisticas, Jugador
from src.gestor.services.gestor_jugadores import GestorJugadores


# Creamos las estadísticas
estadisticas1 = Estadisticas(100, 80, 65, 90, 50)

# Creamos un jugador
jugador1 = Jugador(1, "Lucas", "Guerrero", 12, estadisticas1)


# Mostramos sus datos
print("ID:", jugador1.id_jugador)
print("Nombre:", jugador1.nombre)
print("Clase:", jugador1.clase)
print("Nivel:", jugador1.nivel)

print("Vida:", jugador1.estadisticas.vida)
print("Fuerza:", jugador1.estadisticas.fuerza)
print("Defensa:", jugador1.estadisticas.defensa)
print("Inteligencia:", jugador1.estadisticas.inteligencia)
print("Magia:", jugador1.estadisticas.magia)


# Creamos el gestor
gestor = GestorJugadores()

# Agregamos el jugador a la lista
gestor.agregar_jugador(jugador1)

print("Cantidad de jugadores:", len(gestor.jugadores))
print("Nombre del primer jugador:", gestor.jugadores[0].nombre)


# Buscamos al jugador por su ID
resultado = gestor.buscar_jugador(5)

if resultado is None:
    print("No se encontró el jugador")
else:
    print("Jugador encontrado:", resultado.nombre)


# Modificamos el nivel
gestor.modificar_jugador(1, nivel=20)

print("Nuevo nivel:", jugador1.nivel)


# Modificamos varios datos
gestor.modificar_jugador(
    1,
    nombre="Tomás",
    nivel=30,
    magia=95
)

print("Nombre:", jugador1.nombre)
print("Nivel:", jugador1.nivel)
print("Magia:", jugador1.estadisticas.magia)


# Eliminamos al jugador
gestor.eliminar_jugador(1)

print("Cantidad de jugadores:", len(gestor.jugadores))
