def Caminho(inicial, final):
    estado_atual = final
    lista_acoes =[]
    lista_andares = []
    cont = 0

    while estado_atual.pai != None:
        cont += 1
        lista_acoes.append(estado_atual.acao)
        lista_andares.append(estado_atual.andares)
        estado_atual = estado_atual.pai

    print("\nNúmero de ações: {}".format(cont))
    print("\nAndares iniciais: {}".format(inicial.andares))
    for i in range(1,cont+1):
        print("\nAcao {}: {}".format(i, lista_acoes[-i]))
        print("Andares: {}".format(lista_andares[-i]))
