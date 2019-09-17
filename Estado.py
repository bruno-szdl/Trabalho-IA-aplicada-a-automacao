from itertools import combinations
import pandas as pd

class Estado:
    def __init__(self, andares, pai=None, acao=None):
        self.andares = andares
        self.testado = False
        self.pai = pai
        self.acao = acao
        self.sucessores = []

    def addSucessores(self):
        for i,j in list(combinations([0,1,2,3,4], 2)):
            novos_andares = self.andares*1

            if novos_andares[i] < 42 and novos_andares[j] < 42:
                novos_andares[i] += 8
                novos_andares[j] += 8
                self.sucessores.append(Estado(andares = novos_andares, pai = Estado(self.andares, self.pai, self.acao), acao = "Subir os elevadores {} e {}".format(i+1, j+1)))

                novos_andares = self.andares*1

            if novos_andares[i] > 12 and novos_andares[j] > 12:
                novos_andares[i] -= 13
                novos_andares[j] -= 13
                self.sucessores.append(Estado(andares = novos_andares, pai = Estado(self.andares, self.pai, self.acao), acao = "Descer os elevadores {} e {}".format(i+1, j+1)))
