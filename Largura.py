from Nodo import Nodo
from Caminho import Caminho
import time

#Iniciando contador de tempo
t_i = time.time()

#Definindo nodo inicial e a meta. A meta contém os andares que os elevadores podem estar
inicial = Nodo((20, 20, 22, 24, 21))
meta = (21, 22, 23)
solucao = False

#iniciando a fila
fila = [inicial]

#Contador de nodos e set para guardar quais estados já foram testados
nodos_testados = 0
lista_nodos_testados = set()

#Se não tiver encontrado a solução, pegar o primeiro objeto da fila
while solucao == False:
    nodo_atual = fila[0]
    nodos_testados += 1

    #checando solução
    if all(andar in meta for andar in nodo_atual.estado):
        print('Solução encontrada!')
        print('\nNúmero de nodos testados: {}'.format(nodos_testados))
        Caminho(inicial, nodo_atual)
        solucao = True
    #Se não for estado meta, desenfileirar e adicionar sucessores
    else:
        if nodo_atual.estado not in lista_nodos_testados:
            lista_nodos_testados.add(nodo_atual.estado)
            nodo_atual.addSucessores(meta)
            fila.extend(nodo_atual.sucessores)
        del(fila[0])

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
