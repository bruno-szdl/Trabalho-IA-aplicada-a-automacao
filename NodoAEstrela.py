from itertools import combinations
from Heuristicas import Heuristica1

class Nodo:
    def __init__(self, estado, pai=None, acao=None, custo=0, distancia=1000):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.sucessores = []
        self.custo = custo
        self.distancia = distancia

    def addSucessores(self):
        for i,j in list(combinations([0,1,2,3,4], 2)):
            novos_estados = self.estado*1

            if novos_estados[i] < 42 and novos_estados[j] < 42:
                novos_estados[i] += 8
                novos_estados[j] += 8
                heuristica = Heuristica1(novos_estados, [21, 22, 23])
                self.sucessores.append(Nodo(estado = novos_estados, pai = Nodo(self.estado, self.pai, self.acao), acao = "Subir os elevadores {} e {}".format(i+1, j+1), custo = self.custo + 1, distancia = heuristica))

                novos_estados = self.estado*1

            if novos_estados[i] > 12 and novos_estados[j] > 12:
                novos_estados[i] -= 13
                novos_estados[j] -= 13
                self.sucessores.append(Nodo(estado = novos_estados, pai = Nodo(self.estado, self.pai, self.acao), acao = "Descer os elevadores {} e {}".format(i+1, j+1)))
