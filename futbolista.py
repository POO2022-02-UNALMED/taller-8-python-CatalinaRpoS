from cmath import pi
from deportista import Deportista
from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil

        Futbolista._listaFutbolistas.append(self)
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls._listaFutbolistas = listaFutbolistas

    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(
            Persona.getNombre(self), Deportista.getDeporte(self), Persona.getEdad(self),
            Deportista.getAñosPracticando(self) )