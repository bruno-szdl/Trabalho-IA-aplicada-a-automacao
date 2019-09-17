class Fila:
    def __init__(self):
        self.estados = []

    def enfileirar(self, estado):
        self.estados.append(estado)

    def desenfileirar(self):
        if not self.filaVazia():
            del(self.estados[0])
        else:
            print('A fila ja esta vazia')

    def getPrimeiro(self):
        return self.estados[0]

    def filaVazia(self):
        return (len(self.estados) == 0)
