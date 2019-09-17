from Nodo import Nodo
from Caminho import Caminho
import time



t_i = time.time()

inicial = Nodo([20,20,22,24,21])
meta = [28, 36, 30, 24, 21]
solucao = False
fila = [inicial]
nodos_testados = 0

while solucao == False:
    nodos_testados += 1
    nodo_atual = fila[0]
    print(nodo_atual.estado)
    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    else:
        nodo_atual.addSucessores()
        fila.extend(nodo_atual.sucessores)
        del(fila[0])
        print('Solução não encontrada')
        print(nodos_testados)


t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
