from Nodo import Nodo
from Caminho import Caminho
import time

t_i = time.time()

inicial = Nodo([17, 26, 20, 19, 31])
meta = [21, 22, 23, 24, 25]
solucao = False
profundidade_maxima = 0

while not solucao:
    pilha = [inicial]
    nodos_testados = 0

    while len(pilha) > 0:
        nodo_atual = pilha[-1]
        nodos_testados += 1
        #print(nodo_atual.estado)

        nodo_profundidade = pilha[-1]
        profundidade = 0
        lista_pais = []
        while nodo_profundidade.pai != None:
            profundidade += 1
            lista_pais.append(nodo_profundidade.pai.estado)
            nodo_profundidade = nodo_profundidade.pai

        if all(andar in meta for andar in nodo_atual.estado):
            print('Solução encontrada!')
            print('\nNúmero de nodos testados: {}'.format(nodos_testados))
            print('\nProfundidade da solução: {}'.format(profundidade_maxima))
            Caminho(inicial, nodo_atual)
            solucao = True
            break
        else:
            if (profundidade >= profundidade_maxima) or (nodo_atual.estado in lista_pais):
                del(pilha[-1])
            else:
                nodo_atual.addSucessores()
                del(pilha[-1])
                pilha.extend(nodo_atual.sucessores)
                #print('Solução não encontrada')
                #print(nodos_testados)
    if not solucao:
        print("\nProfundidade máxima {} atingida, aumentando a profundidade máxima para {}.\n".format(profundidade_maxima, profundidade_maxima+1))
    profundidade_maxima += 1

t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
