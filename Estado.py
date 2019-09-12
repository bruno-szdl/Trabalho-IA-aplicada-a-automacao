class Estado:
    def __init__(self, andares):
        self.andares = andares
        self.visitado = False
        self.proxestado = []

    def addProximoEstado(self, estado):
        self.proxestado.append(estado)
