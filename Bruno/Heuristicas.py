def Heuristica1(andares, meta):
    distancia = 0
    for andar in andares:
        if andar not in meta:
            distancia += 1
    return distancia

def Heuristica2(andares, meta):
    distancia = 0
    for andar in andares:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 13 in meta) or (andar - 5 in meta):
            distancia += 2
        else:
            distancia += 3
    return distancia/2
