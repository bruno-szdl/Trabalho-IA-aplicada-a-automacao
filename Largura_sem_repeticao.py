from Estado import Estado
from Caminho import Caminho
import time



t_i = time.time()

inicial = Estado([20,20,22,24,21])
meta = [21, 22, 23]
solucao = False
fila = [inicial]
estados_testados = 0
lista_estados_testados =[]

while solucao == False:
    estado_atual = fila[0]
    estados_testados += 1
    print(estado_atual.andares)

    if all(andar in meta for andar in estado_atual.andares):
        print('Solução encontrada!')
        print('\nNúmero de estados testados: {}'.format(estados_testados))
        Caminho(inicial, estado_atual)
        solucao = True
    else:
        if estado_atual in lista_estados_testados:
            pass
        else:
            lista_estados_testados.append(estado_atual)
            estado_atual.addSucessores()
            fila.extend(estado_atual.sucessores)
            del(fila[0])
            print('Solução não encontrada')
            print(estados_testados)


t_f = time.time()
print('\nTempo de execução: {}'.format(t_f - t_i))
