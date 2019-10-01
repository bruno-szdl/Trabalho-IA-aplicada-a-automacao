from Nodo import Nodo
from Caminho import Caminho
import time

t_i = time.time()

inicial = Nodo([17, 26, 20, 19, 31])
meta = [21, 22, 23, 24, 25]
solucao = False
fila = [inicial]
nodos_testados = 0
lista_nodos_testados =[]

while solucao == False:
    nodo_atual = fila[0]
    nodos_testados += 1
    #print(nodo_atual.estado)

    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    else:
        if nodo_atual in lista_nodos_testados:
            del(fila[0])
        else:
            lista_nodos_testados.append(nodo_atual)
            nodo_atual.addSucessores()
            fila.extend(nodo_atual.sucessores)
            del(fila[0])
            print(nodos_testados)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))