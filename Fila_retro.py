class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.estados = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enfileirar(self, estado):
        if not self.filaCheia():
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim += 1
            self.estados[self.fim] = estado
            self.numeroElementos += 1
        else:
            print('A fila ja esta cheia')

    def desenfileirar(self):
        if not self.filaVazia():
            temp = self.estados[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numeroElementos -= 1
            return temp
        else:
            print('A fila ja esta vazia')

    def getPrimeiro(self):
        return self.estados[self.inicio]

    def filaVazia(self):
        return (self.numeroElementos == 0)

    def filaCheia(self):
        return (self.numeroElementos == self.tamanho)
