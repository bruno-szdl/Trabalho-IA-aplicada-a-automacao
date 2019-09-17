from Fila import Fila
from Estado import Estado
import time

class Largura:
    def __init__(self, inicial):
        self.inicial = inicial
        self.meta = [28, 28, 30, 32, 21]
        self.fila = Fila()
        self.fila.enfileirar(inicial)
        self.testados = [self.inicial]

    def buscar(self):
        primeiro = self.fila.getPrimeiro()
        #print('Primeiro: {}'.format(primeiro.nome))
        print(primeiro.data)
        if all(andar in self.meta for andar in primeiro.andares):
            print('Terminado')
            print(primeiro.data)
        else:
            primeiro.addProximosEstados()
            print("Não achou")
            self.fila.desenfileirar()
            #print('Desenfileirou: {}'.format(temp.nome))
            for a in primeiro.proxestados:
                    print('Verificando se ja foi testado ')
                    testado = False
                    for estado_testado in self.testados:
                        if a.andares == estado_testado.andares:
                            testado = True
                            break
                    if testado == False:
                        self.fila.enfileirar(a)
                        self.testados.append(a)
                        print("tamanho testados: {}".format(len(self.testados)))
            if len(self.fila.estados) > 0:
                Largura.buscar(self)

t_i = time.time()
inicial = Estado([20,20,22,24,21])
largura = Largura(inicial)
largura.buscar()
t_f = time.time()
print('Tempo de execução: {}'.format(t_f - t_i))
