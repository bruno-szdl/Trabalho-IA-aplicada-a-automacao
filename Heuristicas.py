#Heuristicas utilizadas
def Heuristica0(estado, meta):
    return 0

def Heuristica1(estado, meta):
    distancia = 0
    for andar in estado:
        if andar not in meta:
            distancia += 1
    return distancia

def Heuristica2(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        else:
            distancia += 3
    return distancia

def Heuristica2_03(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        else:
            distancia += 3
    return distancia/0.3

def Heuristica3(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or \
            (andar + 3 in meta):
            distancia += 3
        else:
            distancia += 4
    return distancia

def Heuristica3_03(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or \
            (andar + 3 in meta):
            distancia += 3
        else:
            distancia += 4
    return distancia/0.3

def Heuristica4(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or (andar + 3 in meta):
            distancia += 3
        elif (andar + 32 in meta) or (andar + 11 in meta) or (andar - 31 in meta) or (andar - 10 in meta):
            distancia += 4
        else:
            distancia += 5
    return distancia

def Heuristica5(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or (andar + 3 in meta):
            distancia += 3
        elif (andar + 32 in meta) or (andar + 11 in meta) or (andar - 31 in meta) or (andar - 10 in meta):
            distancia += 4
        elif (andar + 40 in meta) or (andar - 19 in meta) or (andar - 44 in meta) or (andar - 2 in meta) or (andar - 23 in meta):
            distancia += 5
        else:
            distancia +=6
    return distancia

def Heuristica5_03(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or (andar + 3 in meta):
            distancia += 3
        elif (andar + 32 in meta) or (andar + 11 in meta) or (andar - 31 in meta) or (andar - 10 in meta):
            distancia += 4
        elif (andar + 40 in meta) or (andar - 19 in meta) or (andar - 44 in meta) or (andar - 2 in meta) or (andar - 23 in meta):
            distancia += 5
        else:
            distancia += 6
    return distancia/0.3

def Heuristica6(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta) or (andar - 13 in meta):
            distancia += 1
        elif (andar + 16 in meta) or (andar - 26 in meta) or (andar - 5 in meta):
            distancia += 2
        elif (andar + 24 in meta) or (andar - 39 in meta) or (andar - 18 in meta) or (andar + 3 in meta):
            distancia += 3
        elif (andar + 32 in meta) or (andar + 11 in meta) or (andar - 31 in meta) or (andar - 10 in meta):
            distancia += 4
        elif (andar + 40 in meta) or (andar - 19 in meta) or (andar - 44 in meta) or (andar - 2 in meta) or (andar - 23 in meta):
            distancia += 5
        elif (andar + 48 in meta) or (andar + 27 in meta) or (andar + 6 in meta) or (andar - 36 in meta) or (andar - 15 in meta):
            distancia += 6
        else:
            distancia += 7
    return distancia
