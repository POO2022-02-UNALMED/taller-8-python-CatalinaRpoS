class Deportista:

    def __init__(self, deporte, anosPracticando):
        self._deporte = deporte
        self._anosPracticando = anosPracticando
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAnosPracticando(self, anosPracticando):
        self._anosPracticando = anosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def getAnosPracticando(self):
        return self._anosPracticando