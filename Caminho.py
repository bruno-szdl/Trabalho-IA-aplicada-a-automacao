def Caminho(inicial, final):
    nodo_atual = final
    lista_acoes =[]
    lista_estados = []
    cont = 0

    while nodo_atual.pai != None:
        cont += 1
        lista_acoes.append(nodo_atual.acao)
        lista_estados.append(nodo_atual.estado)
        nodo_atual = nodo_atual.pai

    print("\nNúmero de ações: {}".format(cont))
    print("\nAndares iniciais: {}".format(inicial.estado))
    for i in range(1,cont+1):
        print("\nAcao {}: {}".format(i, lista_acoes[-i]))
        print("Andares: {}".format(lista_estados[-i]))
