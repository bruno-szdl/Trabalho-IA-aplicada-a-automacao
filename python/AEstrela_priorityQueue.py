from NodoAEstrela import Nodo
from Caminho import Caminho
from queue import PriorityQueue
import time

t_i = time.time()

inicial = Nodo([20, 20, 22, 24, 21])
meta = [21, 22, 23]
solucao = False
fila_prioritaria = PriorityQueue()
fila_prioritaria.put(inicial.custo_total, inicial)
nodos_testados = 0
lista_nodos_testados = []

while solucao == False:
    nodo_atual = fila_prioritaria.get()
    print("andares: {}".format(nodo_atual.estado))
    print("custo: {}".format(nodo_atual.custo))
    print("distancia: {}".format(nodo_atual.distancia))
    print("custo total: {}".format(nodo_atual.custo_total))
    nodos_testados += 1
    #print(nodo_atual.estado)

    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    else:
        if nodo_atual in lista_nodos_testados:
            pass
        else:
            lista_nodos_testados.append(nodo_atual)
            nodo_atual.addSucessores(meta)
            for i in len(nodo_atual.sucessores):
                fila_prioritaria.put(nodo_atual.sucessores[i].custo_total, nodo_atual.sucessores[i])
            print(nodos_testados)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
