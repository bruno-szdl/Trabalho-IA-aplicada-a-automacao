from Nodo import Nodo
from Caminho import Caminho
import time

#Iniciando contador de tempo
t_i = time.time()

#Definindo nodo inicial e a meta. A meta contém os andares que os elevadores podem estar
inicial = Nodo((20, 20, 22, 24, 21))
meta = (21, 22, 23)
solucao = False

#iniciando a pilha
pilha = [inicial]

#Contador de nodos e set para guardar quais estados já foram testados
nodos_testados = 0
estados_testados = set()

#Se não tiver encontrado a solução, pegar o último objeto da pilha
while solucao == False:
    nodo_atual = pilha[-1]
    nodos_testados += 1

    #checando solução
    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    #Se não for estado meta, desempilhar e adicionar sucessores
    else:
        if nodo_atual.estado not in estados_testados:
            del(pilha[-1])
        else:
            estados_testados.add(nodo_atual.estado)
            nodo_atual.addSucessores(meta)
            del(pilha[-1])
            pilha.extend(nodo_atual.sucessores)

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
