class Estadisticas:
    """Estadísticas de un jugador, con valores enteros entre 0 y 100."""

    _vida: int
    _fuerza: int
    _defensa: int
    _inteligencia: int
    _magia: int

    def __init__(
        self,
        vida: int,
        fuerza: int,
        defensa: int,
        inteligencia: int,
        magia: int,
    ) -> None:
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.magia = magia

    @staticmethod
    def _validar(valor: int, atributo: str) -> None:
        if type(valor) is not int or not 0 <= valor <= 100:
            raise ValueError(f"{atributo} debe ser un entero entre 0 y 100.")

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int) -> None:
        self._validar(valor, "La vida")
        self._vida = valor

    @property
    def fuerza(self) -> int:
        return self._fuerza

    @fuerza.setter
    def fuerza(self, valor: int) -> None:
        self._validar(valor, "La fuerza")
        self._fuerza = valor

    @property
    def defensa(self) -> int:
        return self._defensa

    @defensa.setter
    def defensa(self, valor: int) -> None:
        self._validar(valor, "La defensa")
        self._defensa = valor

    @property
    def inteligencia(self) -> int:
        return self._inteligencia

    @inteligencia.setter
    def inteligencia(self, valor: int) -> None:
        self._validar(valor, "La inteligencia")
        self._inteligencia = valor

    @property
    def magia(self) -> int:
        return self._magia

    @magia.setter
    def magia(self, valor: int) -> None:
        self._validar(valor, "La magia")
        self._magia = valor


class Jugador:
    """Representa un jugador del sistema."""

    _id_jugador: int
    _nombre: str
    _clase: str
    _nivel: int
    _estadisticas: Estadisticas

    def __init__(
        self,
        id_jugador: int,
        nombre: str,
        clase: str,
        nivel: int,
        estadisticas: Estadisticas,
    ) -> None:
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.estadisticas = estadisticas

    @property
    def id_jugador(self) -> int:
        return self._id_jugador

    @id_jugador.setter
    def id_jugador(self, valor: int) -> None:
        if type(valor) is not int or valor < 1:
            raise ValueError("El ID debe ser un entero positivo.")
        self._id_jugador = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self._nombre = valor.strip()

    @property
    def clase(self) -> str:
        return self._clase

    @clase.setter
    def clase(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La clase debe ser un texto no vacío.")
        self._clase = valor.strip()

    @property
    def nivel(self) -> int:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: int) -> None:
        if type(valor) is not int or not 1 <= valor <= 100:
            raise ValueError("El nivel debe ser un entero entre 1 y 100.")
        self._nivel = valor

    @property
    def estadisticas(self) -> Estadisticas:
        return self._estadisticas

    @estadisticas.setter
    def estadisticas(self, valor: Estadisticas) -> None:
        if not isinstance(valor, Estadisticas):
            raise ValueError("Se necesita un objeto Estadisticas.")
        self._estadisticas = valor
