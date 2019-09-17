from Fila import Fila
from Estado import Estado
from printCaminho import printCaminho
import time

class Largura:
    def __init__(self, inicial):
        self.inicial = inicial
        self.meta = [28, 28, 30, 27, 16]
        self.fila = Fila()
        self.fila.enfileirar(inicial)
        self.testados = [self.inicial]

    def printCaminho(self, Estado):
        self.Estado = Estado
        estado_atual = Estado
        lista_acoes =[]
        lista_andares = []
        cont = 0

        while estado_atual.pai != None:
            cont += 1
            lista_acoes.append(estado_atual.acao)
            lista_andares.append(estado_atual.andares)
            estado_atual = estado_atual.pai

        print("\nNúmero de ações: {}".format(cont))
        print("\nAndares iniciais: {}".format(self.inicial.andares))
        for i in range(1,cont+1):
            print("\nAcao {}: {}".format(i, lista_acoes[-i]))
            print("Andares: {}".format(lista_andares[-i]))

    def buscar(self):
        primeiro = self.fila.getPrimeiro()

        if all(andar in self.meta for andar in primeiro.andares):
            print('Solução econtrada!')
            Largura.printCaminho(self, primeiro)
        else:
            primeiro.addSucessores()
            self.fila.desenfileirar()
            for sucessor in primeiro.sucessores:
                    testado = False
                    for estado_testado in self.testados:
                        if sucessor.andares == estado_testado.andares:
                            testado = True
                            break
                    if testado == False:
                        self.fila.enfileirar(sucessor)
                        self.testados.append(sucessor)
                        print("\nEstados testados: {}".format(len(self.testados)))
            if len(self.fila.estados) > 0:
                Largura.buscar(self)
            else:
                print('Solução não encontrada')



t_i = time.time()
inicial = Estado([20,20,22,24,21])
Largura(inicial).buscar()
t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
