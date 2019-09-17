from Estado import Estado
from Caminho import Caminho
import time



t_i = time.time()

inicial = Estado([20,20,22,24,21])
meta = [28, 28, 22, 24, 21]
solucao = False
pilha = [inicial]
estados_testados = 0
lista_andares_testados =[]

while solucao == False:
    estado_atual = pilha[-1]
    estados_testados += 1
    print(estado_atual.andares)

    if all(andar in meta for andar in estado_atual.andares):
        print('Solução encontrada!')
        print('\nNúmero de estados testados: {}'.format(estados_testados))
        Caminho(inicial, estado_atual)
        solucao = True
    else:
        if estado_atual.andares in lista_andares_testados:
            del(pilha[-1])
        else:
            lista_andares_testados.append(estado_atual.andares)
            estado_atual.addSucessores()
            del(pilha[-1])
            pilha.extend(estado_atual.sucessores)
            print('Solução não encontrada')
            print(estados_testados)


t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
