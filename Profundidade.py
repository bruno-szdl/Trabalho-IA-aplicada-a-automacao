from Nodo import Nodo
from Caminho import Caminho
import time

t_i = time.time()

inicial = Nodo([20, 20, 22, 24, 21])
meta = [21, 22, 23]
solucao = False
pilha = [inicial]
nodos_testados = 0
lista_estado_testados =[]

while solucao == False:
    nodo_atual = pilha[-1]
    nodos_testados += 1
    #print(nodo_atual.estado)

    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    else:
        if nodo_atual.estado in lista_estado_testados:
            del(pilha[-1])
        else:
            lista_estado_testados.append(nodo_atual.estado)
            nodo_atual.addSucessores()
            del(pilha[-1])
            pilha.extend(nodo_atual.sucessores)
            #print('Solução não encontrada')
            print(nodos_testados)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
