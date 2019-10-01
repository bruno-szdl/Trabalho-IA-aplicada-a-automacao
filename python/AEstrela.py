from NodoAEstrela import Nodo
from Caminho import Caminho
import time

t_i = time.time()

inicial = Nodo([20, 20, 22, 24, 21])
meta = [21, 22, 23]
solucao = False
fila = [inicial]
nodos_testados = 0
set_estados_testados = set()

while solucao == False:
    nodo_atual = fila[0]
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
        if tuple(nodo_atual) in set_estados_testados:
            del(fila[0])
        else:
            set_estados_testados.add(tuple(nodo_atual))
            nodo_atual.addSucessores(meta)
            fila.extend(nodo_atual.sucessores)
            del(fila[0])
            fila.sort(key=lambda x: x.custo_total)
            print(nodos_testados)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
