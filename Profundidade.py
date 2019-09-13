from Pilha import Pilha
from Estado import Estado

class Profundidade:
    def __init__(self, inicial):
        self.inicial = inicial
        self.meta = [28, 22, 24, 21]
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicial)
        self.testados = [self.inicial]

    def buscar(self):
        topo = self.pilha.getTopo()
        print(topo.data)

        if all(andar in self.meta for andar in topo.andares):
            print('Terminado')
            print(topo.data)
        else:
            topo.addProximosEstados()
            for a in topo.proxestados:
                print('Verificando se já testado')
                testado = False
                for estado_testado in self.testados:
                    if a.andares == estado_testado.andares:
                        testado = True
                        break
                if testado == False:
                    self.pilha.empilhar(a)
                    self.testados.append(a)
                    print("tamanho testados: {}".format(len(self.testados)))
                    Profundidade.buscar(self)
        self.pilha.desempilhar()

inicial = Estado([20,20,22,24,21])
profundidade = Profundidade(inicial)
profundidade.buscar()

