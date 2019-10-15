#Heuristicas utilizadas
def Heuristica0(estado, meta):
    return 0

def Heuristica1(estado, meta):
    distancia = 0
    for andar in estado:
        if andar not in meta:
            distancia += 800
    return distancia

def Heuristica2(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 16 in meta):
            distancia += 1600
        else:
            distancia += 2400
    return distancia


def Heuristica2_03(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 16 in meta):
            distancia += 1600
        else:
            distancia += 2400
    return distancia/0.3


def Heuristica2_085(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 16 in meta):
            distancia += 1600
        else:
            distancia += 2400
    return distancia/0.85


def Heuristica3(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar + 16 in meta):
            distancia += 1600
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 24 in meta):
            distancia += 2400
        elif (andar - 39 in meta):
            distancia += 97.5
        elif (andar - 18 in meta):
            distancia += 865
        elif (andar + 3 in meta):
            distancia += 1635.2
        else:
            distancia += 3200
    return distancia

def Heuristica4(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar + 16 in meta):
            distancia += 1600
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 24 in meta):
            distancia += 2400
        elif (andar - 39 in meta):
            distancia += 97.5
        elif (andar - 18 in meta):
            distancia += 865
        elif (andar + 3 in meta):
            distancia += 1632.5
        elif (andar + 32 in meta):
            distancia += 3200
        elif (andar + 11 in meta):
            distancia += 2432.5
        elif (andar - 31 in meta):
            distancia += 897.5
        elif (andar - 10 in meta):
            distancia += 1665
        else:
            distancia += 4000
    return distancia


def Heuristica4_06(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar + 16 in meta):
            distancia += 1600
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 24 in meta):
            distancia += 2400
        elif (andar - 39 in meta):
            distancia += 97.5
        elif (andar - 18 in meta):
            distancia += 865
        elif (andar + 3 in meta):
            distancia += 1632.5
        elif (andar + 32 in meta):
            distancia += 3200
        elif (andar + 11 in meta):
            distancia += 2432.5
        elif (andar - 31 in meta):
            distancia += 897.5
        elif (andar - 10 in meta):
            distancia += 1665
        else:
            distancia += 4000
    return distancia/0.6


def Heuristica5(estado, meta):
    distancia = 0
    for andar in estado:
        if andar in meta:
            pass
        elif (andar + 8 in meta):
            distancia += 800
        elif (andar - 13 in meta):
            distancia += 32.5
        elif (andar + 16 in meta):
            distancia += 1600
        elif (andar - 26 in meta):
            distancia += 65
        elif (andar - 5 in meta):
            distancia += 832.5
        elif (andar + 24 in meta):
            distancia += 2400
        elif (andar - 39 in meta):
            distancia += 97.5
        elif (andar - 18 in meta):
            distancia += 865
        elif (andar + 3 in meta):
            distancia += 1632.5
        elif (andar + 32 in meta):
            distancia += 3200
        elif (andar + 11 in meta):
            distancia += 2432.5
        elif (andar - 31 in meta):
            distancia += 897.5
        elif (andar - 10 in meta):
            distancia += 1665
        elif (andar + 40 in meta):
            distancia += 4000
        elif (andar - 19 in meta):
            distancia += 3232.5
        elif (andar - 44 in meta):
            distancia += 930
        elif (andar - 2 in meta):
            distancia += 2465
        elif (andar - 23 in meta):
            distancia += 1697.5
        else:
            distancia += 4800
    return distancia
