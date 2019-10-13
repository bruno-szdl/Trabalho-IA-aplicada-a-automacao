from Nodo import Nodo
from Caminho import Caminho
import time

t_i = time.time()

inicial = Nodo((20, 20, 22, 24, 21))
meta = (21, 22, 23)
solucao = False
fila = [inicial]
nodos_testados = 0
set_estados_testados = set()

while solucao == False:
    nodo_atual = fila[0]
    nodos_testados += 1

    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    else:
        if tuple(nodo_atual.estado) in set_estados_testados:
            del(fila[0])
        else:
            set_estados_testados.add(nodo_atual.estado)
            nodo_atual.addSucessores(meta)
            fila.extend(nodo_atual.sucessores)
            del(fila[0])
            fila.sort(key=lambda n: n.custo_total)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
