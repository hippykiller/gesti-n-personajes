class Estadisticas:

    def __init__(self, vida, fuerza, defensa, inteligencia, magia):
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.magia = magia
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nueva_vida):
        if 0 <= nueva_vida <= 100:
            self._vida = nueva_vida
        else:
            raise ValueError("La vida debe estar entre 0 y 100.")
        
        
    @property
    def fuerza(self):
        return self._fuerza
            
    @fuerza.setter
    def fuerza(self, nueva_fuerza):
        if 0 <= nueva_fuerza <= 100:
            self._fuerza = nueva_fuerza
        else:
            raise ValueError( "la fuerza debe estar entre 0 y 100")
    
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, nueva_defensa):
        if 0 <= nueva_defensa <= 100:
            self._defensa = nueva_defensa
        else:
            raise ValueError( "la defensa debe estar entre 0 y 100")
        
    @property
    def inteligencia(self):
        return self._inteligencia
    
    @inteligencia.setter
    def inteligencia(self, nueva_inteligencia):
        if 0 <= nueva_inteligencia <= 100:
            self._inteligencia = nueva_inteligencia
        else:
            raise ValueError( "la inteligencia debe estar entre 0 y 100")
    
    @property
    def magia(self):
        return self._magia
    
    @magia.setter
    def magia(self, nueva_magia):
        if 0 <= nueva_magia <= 100:
            self._magia = nueva_magia
        else:
            raise ValueError( "la magia debe estar entre 0 y 100")



class Jugador:
    
    def __init__(self, id_jugador, nombre, clase, nivel, estadisticas):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.estadisticas = estadisticas
    
    @property
    def id_jugador(self):
        return self._id_jugador
    
    @id_jugador.setter
    def id_jugador(self, nueva_id_jugador):
        if isinstance(nueva_id_jugador, int) and nueva_id_jugador >= 1:
            self._id_jugador = nueva_id_jugador
        else:
            raise ValueError("El ID del jugador debe ser un numero entero positivo igual o mayor a 1")
    
    
    @property
    def nombre(self):
            return self._nombre
        
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre del jugador debe ser un texto no vacío.")
    
    
    @property
    def clase(self):
        return self._clase
    
    @clase.setter
    def clase(self, nueva_clase):
        if isinstance(nueva_clase, str) and nueva_clase.strip():
            self._clase = nueva_clase.strip()
        else:
            raise ValueError("La clase del jugador debe ser un texto no vacío.")
    
    
    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, nuevo_nivel):
        if isinstance(nuevo_nivel, int) and 1 <= nuevo_nivel <= 100:
            self._nivel = nuevo_nivel
        else:
            raise ValueError( "El nivel debe ser entre 1 y 100")
    
    
    @property
    def estadisiticas(self):
        return self._estadisticas
    
    @estadisiticas.setter
    def estadisticas(self, nuevas_estadisticas):
        if isinstance (nuevas_estadisticas, Estadisticas):
            self._estadisticas = nuevas_estadisticas
        else:
            raise ValueError( "las estadisticas deben ser un objeto de tipo Estadisticas.")