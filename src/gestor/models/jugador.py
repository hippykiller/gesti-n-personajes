from dataclasses import dataclass


@dataclass
class Jugador:
    """Ficha de socio del sistema."""

    id_jugador: int
    nombre_user: str
    contrasena_hash: str
    personaje_elegido: str  # texto; más adelante puede ser clase Personaje
    id_inventario: int
    estado_cuenta: bool = True  # True = activo
