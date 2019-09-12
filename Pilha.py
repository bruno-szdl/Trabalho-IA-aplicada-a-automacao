class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.estados = [None] * self.tamanho
        self.topo = -1

    def empilhar(self, estado):
        if not self.pilhaCheia():
            self.topo += 1
            self.estados[self.topo] = estado
        else:
            print('A pilha ja esta cheia')

    def desempilhar(self):
        if not self.pilhaVazia():
            temp = self.estados[self.topo]
            self.topo -= 1
            return temp
        else:
            print('A pilha ja esta cheia')
            return None
    def getTopo(self):
        return self.estados[self.topo]

    def pilhaVazia(self):
        return (self.topo == -1)

    def pilhaCheia(self):
        return (self.topo == self.tamanho -1)
