"""Modelo de datos del personaje que elige un jugador."""

from dataclasses import dataclass
from enum import Enum


class ClasePersonaje(Enum):
    """Clases disponibles para un personaje."""

    GUERRERO = "Guerrero"
    MAGO = "Mago"
    ARQUERO = "Arquero"


@dataclass
class Personaje:
    """Un personaje del videojuego, con sus atributos de combate."""

    id_personaje: int
    nombre: str
    clase: ClasePersonaje
    nivel: int = 1
    vida: int = 100
    ataque: int = 10
    defensa: int = 5

    def __post_init__(self) -> None:
        """Valida los datos apenas se crea el personaje."""
        self.nombre = self.nombre.strip()
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if self.nivel < 1:
            raise ValueError("El nivel debe ser al menos 1.")
        if self.vida < 0:
            raise ValueError("La vida no puede ser negativa.")
        if self.ataque < 0:
            raise ValueError("El ataque no puede ser negativo.")
        if self.defensa < 0:
            raise ValueError("La defensa no puede ser negativa.")

    def esta_vivo(self) -> bool:
        """Indica si al personaje le queda vida."""
        return self.vida > 0

    def recibir_dano(self, dano: int) -> None:
        """Resta vida al personaje sin dejarla por debajo de cero."""
        if dano < 0:
            raise ValueError("El daño no puede ser negativo.")
        self.vida = max(self.vida - dano, 0)

    def subir_nivel(self) -> None:
        """Aumenta el nivel del personaje en uno."""
        self.nivel += 1
