from itertools import combinations
import pandas as pd

class Estado:
    def __init__(self, andares):
        self.andares = andares
        self.testado = False
        self.proxestados = []

        data = {
        'Elevador':['1', '2', '3', '4', '5'],
        'Andar': [self.andares[0], self.andares[1], self.andares[2], self.andares[3], self.andares[4]],
        }
        self.data = pd.DataFrame(data)

    def addProximosEstados(self):
        for i,j in list(combinations([0,1,2,3,4], 2)):
            novos_andares = self.andares*1


            if novos_andares[i] < 42 and novos_andares[j] < 42:
                novos_andares[i] += 8
                novos_andares[j] += 8
                self.proxestados.append(Estado(novos_andares))

                novos_andares = self.andares*1

            if novos_andares[i] > 12 and novos_andares[j] > 12:
                novos_andares[i] -= 13
                novos_andares[j] -= 13
                self.proxestados.append(Estado(novos_andares))
