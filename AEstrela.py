from Nodo import Nodo
from Caminho import Caminho
from PriorityQueue import PriorityQueue
import time

#Iniciando contador de tempo
t_i = time.time()

#Definindo nodo inicial e a meta. A meta contém os andares que os elevadores podem estar
inicial = Nodo((17, 26, 20, 19, 31))
meta = (21, 22, 23, 24, 25)
solucao = False

#Gerando a fila prioritária
fronteira = PriorityQueue('min', lambda n: n.custo_total)
fronteira.append(inicial)

#Contador de nodos e set para guardar quais estados já foram testados
nodos_testados = 0
estados_testados = set()

#Se não tiver encontrado a solução, pegar o primeiro objeto da fila
while solucao == False:
    nodo_atual = fronteira.pop()
    nodos_testados += 1

    #Se esse estado for um estado meta, mostrar o caminho e quantos nodos foram testados
    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    # Se não for um estado meta, gerar os sucessores e colocá-los na fila prioritária de acordo com o custo
    else:
        if nodo_atual not in estados_testados:
            estados_testados.add(nodo_atual)
            nodo_atual.addSucessores(meta)
            fronteira.extend(nodo_atual.sucessores)
            print(nodos_testados)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
