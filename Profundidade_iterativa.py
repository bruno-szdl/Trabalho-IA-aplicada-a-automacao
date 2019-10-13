from Nodo import Nodo
from Caminho import Caminho
import time

#Iniciando contador de tempo
t_i = time.time()

#Definindo nodo inicial e a meta. A meta contém os andares que os elevadores podem estar
inicial = Nodo((20, 20, 22, 24, 21))
meta = (21, 22, 23)
solucao = False

#Iniciando profundidade máxima em 0
profundidade_maxima = 0

while not solucao:
    pilha = [inicial]

    #Contador de nodos e set para guardar quais estados já foram testados
    #dentro do while para zerar cada vez que mudar a profundidade máxima
    nodos_testados = 0
    set_estados_testados = set()

    while len(pilha) > 0:
        nodo_atual = pilha[-1]
        nodos_testados += 1

        #checando profundidade do nodo
        nodo_profundidade = pilha[-1]
        profundidade = 0
        while nodo_profundidade.pai != None:
            profundidade += 1
            nodo_profundidade = nodo_profundidade.pai

        #checando solução
        if all(andar in meta for andar in nodo_atual.estado):
            print('Solução encontrada!')
            print('\nNúmero de nodos testados: {}'.format(nodos_testados))
            print('\nProfundidade da solução: {}'.format(profundidade_maxima))
            Caminho(inicial, nodo_atual)
            solucao = True
            break
        #checando se o nodo já foi explorado ou está na profundidade máxima, se não ele é expandido
        else:
            if (profundidade >= profundidade_maxima) or nodo_atual.estado in set_estados_testados:
                del(pilha[-1])
            else:
                set_estados_testados.add(nodo_atual.estado)
                nodo_atual.addSucessores(meta)
                del(pilha[-1])
                pilha.extend(nodo_atual.sucessores)

    #Caso todos os nodos sejam explorados e não haja solução, a profundidade máxima é aumentada
    if not solucao:
        print("\nProfundidade máxima {} atingida, aumentando a profundidade máxima para {}.\n".format(profundidade_maxima, profundidade_maxima+1))
    profundidade_maxima += 1

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
