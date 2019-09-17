from Estado import Estado
from Caminho import Caminho
import time

t_i = time.time()

inicial = Estado([20,20,22,24,21])
meta = [21, 22, 23]
solucao = False
profundidade_maxima = 0

while not solucao:

    pilha = [inicial]
    estados_testados = 0
    lista_andares_testados =[]

    while len(pilha) > 0:

        estado_atual = pilha[-1]
        estados_testados += 1
       # print(estado_atual.andares)

        estado_profundidade = pilha[-1]
        profundidade = 0
        while estado_profundidade.pai != None:
            profundidade += 1
            estado_profundidade = estado_profundidade.pai

        if all(andar in meta for andar in estado_atual.andares):
            print('Solução encontrada!')
            print('\nNúmero de estados testados: {}'.format(estados_testados))
            print('\nProfundidade da solução: {}'.format(profundidade_maxima))
            Caminho(inicial, estado_atual)
            solucao = True
            break
        else:
            if (profundidade >= profundidade_maxima) or (estado_atual.andares in lista_andares_testados):
                del(pilha[-1])
            else:
                lista_andares_testados.append(estado_atual.andares)
                estado_atual.addSucessores()
                del(pilha[-1])
                pilha.extend(estado_atual.sucessores)
                #print('Solução não encontrada')
                #print(estados_testados)
    if not solucao:
        print("\nProfundidade máxima {} atingida, aumentando a profundidade máxima para {}.\n".format(profundidade_maxima, profundidade_maxima+1))
    profundidade_maxima += 1



t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
