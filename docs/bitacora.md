# Bitácora — gestión-personajes

FECHA: 22/10/2026  
FASE: modelos de datos (Personaje en curso + arranque de Jugador)

HECHO Y MERGEADO: setup + CI en verde (`main`). Esqueleto `src/gestor` (`models`, `structures`, `services`, `ui`), `tests`, `data`, `docs`. Nadie sube directo a `main`; se trabaja en rama y Pull Request.

EN CURSO: rama `feat/modelo-personaje` (Personaje + ClasePersonaje, 12 tests en `tests/test_personaje.py`). En local, sin commitear: molde `Jugador` (`src/gestor/models/jugador.py`) + 2 tests en `tests/test_jugador.py` (pytest: 2 passed). Pendiente: decisión del equipo sobre si Personaje va como clase aparte o como dato simple dentro de Jugador. El borrador sigue en https://github.com/hippykiller/gesti-n-personajes/pull/2

DECISIONES TOMADAS:
- `Jugador` es un `@dataclass` (ficha de socio), no un servicio: vive en `src/gestor/models/`, no en `services/` ni en `ui/`.
- Campos: `id_jugador`, `nombre_user`, `contrasena_hash`, `personaje_elegido: str` (texto por ahora), `id_inventario`, `estado_cuenta: bool = True` (activo por defecto; `False` = dada de baja).
- Los tests no se pegan dentro del molde: el modelo no se importa a sí mismo (eso rompió pytest con import circular). Molde en `jugador.py`, asserts en `test_jugador.py`.
- Python del equipo: 3.12 a 3.14 (no 3.15). Entorno local: 3.14.6.

MI PIEZA: `Jugador` (dataclass + `estado_cuenta` + tests de creación activa/inactiva). Hash real de contraseña y Faker: todavía no. Issue: [#__]. Rama actual: `feat/modelo-personaje`

PRÓXIMO MICRO-PASO: `git add` de `jugador.py` y `test_jugador.py`, commit en esta rama (no en `main`), y después definir si `personaje_elegido` sigue como `str` o apunta a la clase `Personaje`.

DUDAS ABIERTAS:
- ¿El equipo confirma clase `Personaje` aparte (sí) o solo un string dentro de `Jugador` (no)?
- ¿El TP acepta `@dataclass` o el profe quiere `__init__` a mano?
- Número de issue de la pieza Jugador / hash / Faker.
