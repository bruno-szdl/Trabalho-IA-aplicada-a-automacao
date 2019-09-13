from Fila import Fila
from Estado import Estado

class Largura:
    def __init__(self, inicial):
        self.inicial = inicial
        self.meta = [28, 22, 24, 21]
        self.fronteira = Fila(10000)
        self.fronteira.enfileirar(inicial)
        self.achou = False
        self.testados = [self.inicial]

    def buscar(self):
        primeiro = self.fronteira.getPrimeiro()
        primeiro.addProximosEstados()
        #print('Primeiro: {}'.format(primeiro.nome))

        if all(andar in self.meta for andar in primeiro.andares):
            self.achou = True
            print('Terminado')
            print(primeiro.data)
        else:
            temp = self.fronteira.desenfileirar()
            #print('Desenfileirou: {}'.format(temp.nome))

            for a in primeiro.proxestados:
                if self.achou == False:
                    print('Verificando se ja foi testado ')
                    testado = False
                    for testado in self.testados:
                        if a.andares == testado.andares:
                            testado = True
                            break
                    if testado == False:
                        self.fronteira.enfileirar(a)
                        self.testados.append(a)
                        print(len(self.testados))
                        print(self.testados[-1].data)
            if self.fronteira.numeroElementos > 0:
                Largura.buscar(self)

inicial = Estado([20,20,22,24,21])
largura = Largura(inicial)
largura.buscar()
