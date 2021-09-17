from os import system
from random import randint

def titol(paraula = "CONECTA 4"):
    amplitud = 80
    for i in range(amplitud):
        print('#', end='')
    print("#")
    for i in range(int(amplitud/2)-int(len(paraula)/2)):
        print('#', end='')
    print(paraula, end='')
    for i in range(int(amplitud/2)-int(len(paraula)/2)):
        print('#', end='')
    print()
    for i in range(amplitud):
        print('#', end='')
    print("#")

def menu(jugador):
    opcio = "Z"
    while opcio.upper() not in ['A','B','C']:
        system("cls")
        titol()
        print("Què vols fer?")
        print("A.Jugar una partida")
        print("B.Veure el ranking de jugadors")
        print("C.Sortir")
        opcio = input()
    if opcio.upper() == "B":
        system("cls")
        print('Nom:\t', end = '')
        print('Partides guanyades:\t', end = '')
        print('Partides perdudes:\t', end = '')
        print('Partides empatades:\t', end = '')
        print()
        for i in range(len(jugador)):
            print(f"{jugador[i]['nom']}\t\t\t", end = '')
            print(f"{jugador[i]['partides']['guanyades']}\t\t\t", end = '')
            print(f"{jugador[i]['partides']['perdudes']}\t\t\t", end = '')
            print(f"{jugador[i]['partides']['empatades']}\t\t\t", end = '')
            print()
        input()
        menu(jugador)
    elif opcio.upper() == "C":
        system("cls")
        titol()
        exit("Fins la pròxima!")


def crear_taulell(files = 7, columnes = 6):
    '''
    Només utilitzar per crear el taulell
    :param files:
    :param columnes:
    :return:
    '''
    taulell = []
    fila = []
    for i in range(columnes):
        fila.append(" ")
    for i in range(files):
        taulell.append(fila[:])
    return taulell

def repeticio_caracters(c1, columnes, opcio = 1, c2 = "", c3 = ""):
    if opcio == 1:
        print('\t', end='')
        for i in range(columnes):
            print(f"{c1}"*(3+len((str(i)))), end = '')
    elif opcio == 2:
        print('\t', end='|')
        for j in range(columnes):
            print(f"{c1}"*len(str(j+1))+f"{c2}", end='|')
    print(c3)


def mostrar_taulell(taulell, files, columnes, jugador, fitxes, juga, torn):
    '''
    Per mostrar el taulell amb columnes i files
    :param taulell:
    :return:
    '''
    system("cls")
    titol()
    repeticio_caracters("-", columnes,1,"","-")
    for i in range(files):
        repeticio_caracters(" ", columnes, 2, "  ")
        print('\t', end='|')
        for j in range(columnes):
            print(f" " * len(str(j + 1)) + f"{taulell[i][j]} ", end='|')
        print()
        repeticio_caracters(" ", columnes, 2, "  ")
        repeticio_caracters("-", columnes, 1,"","-")
    print('\t', end='')
    for i in range(columnes):
        print("_"*(3+len((str(i)))), end = '')
    print("_")
    print('\t|', end='')
    for x in range(columnes):
        print(f" {x + 1} ", end='|')
    print(f'\t{jugador[juga]["nom"]}: o[{fitxes[torn]}] \t Màquina: x[{fitxes[not torn]}]')
    print('\t', end='')
    for i in range(int(columnes/2)):
        print("洛"*(3+len((str(i)))), end = '')
    if columnes % 2 == 1:
        print("洛", end = '')
    print("洛")

def fer_jugada(torn, columnes, taulell, files):
    '''
    Aquesta funció només fa la jugada, no la comprova.
    :param torn:
    :param columnes:
    :return:
    '''
    if torn == True: #tira el jugador
        jugada = ""
        while not jugada.isdigit() or int(jugada) < 1 or int(jugada) > columnes or not validar_jugada(int(jugada),taulell):
            jugada = input("Introdueix la columna on vols introdüir la teva fitxa: ")
        jugada = int(jugada)
        for i in range(files):
            if taulell[i][jugada-1] != " ":
                return (i - 1, jugada - 1)
        return (files-1, jugada - 1)
    else:
        # fer inteligencia artificial
        if guanyar(taulell, "x", 5) != False: #pot guanyar la màquina
            input("Msg màquina: I així guanyo.")
            jugada = guanyar(taulell, "x", 5)
            return jugada
        elif guanyar(taulell, "o", 5) != False: #pot guanyar el jugador
            input("Msg màquina: I així evito que guanyis.")
            jugada = guanyar(taulell, "o", 5)
            return jugada
        else:
            input("Msg màquina: Tiro random XD.")
            jugada = randint(1,columnes)
            for i in range(files):
                if taulell[i][jugada-1] != " ":
                    return (i - 1, jugada - 1)
            return files - 1, jugada - 1


def validar_jugada(jugada, taulell):
    '''
    Valida la jugada.
    :param jugada:
    :return:
    '''
    if taulell[0][jugada-1] == " ":
        return True
    else:
        return False


def fitxa(torn):
    '''
    Posa la fitxa correcta
    :param torn:
    :param :
    :return:
    '''
    fitxes = ['x', 'o']
    return fitxes[torn]

def guanyar(taulell, fitxa, sw = 0):
    '''
    Comprova si la jugada és guanyadora. O si pot guanyar.
    :param :
    :return:
    '''
    fitxes = []  # fitxes al taulell
    for i in range(len(taulell)):
        for j in range(len(taulell[i])):
            if taulell[i][j] != " ":
                fitxes.append((i, j))
    calc = 4 # per calcular si ha guanyat (4) o pot guanyar (3)
    # sw = Switch per l'última part
    z = 0 # contador del bucle, també utilitzat per scanejar posicións
    if len(fitxes) != 0:
        while z < len(fitxes):
            comptador = 0
            # columnes
            for j in range(fitxes[z][0] - 3, fitxes[z][0]+1):
                if j < 0:
                    break
                if taulell[j][fitxes[z][1]] == fitxa:
                    comptador += 1
                if comptador == calc:
                    if calc == 3:
                        for i in range(fitxes[z][0] - 3, fitxes[z][0]+1):
                            if taulell[i][fitxes[z][1]] == " ":
                                return (i, fitxes[z][1])
                    else:
                        return True
            # Files
            comptador = 0
            for j in range(fitxes[z][1] - 3, fitxes[z][1]+1):
                if j < 0:
                    break
                if taulell[fitxes[z][0]][j] == fitxa:
                    comptador += 1
                if comptador == calc:
                    if calc == 3:
                        input(3)
                        for i in range(fitxes[z][1] - 3, fitxes[z][1] + 1):
                            if taulell[fitxes[z][0]][i] == " ":
                                if fitxes[z][0] + 1 > len(taulell) - 1 or taulell[fitxes[z][0]+1][i] != " ":
                                    return (fitxes[z][0], i)
                    else:
                        return True
            # Diagonals
            '''
            Ordre de comprovció
                    #
                #
            ##
            '''
            comptador = 0
            #print("1")
            for j in range(4):
                if fitxes[z][0] - j < 0 or fitxes[z][1] + j + 1 > len(taulell[0]) - 1:
                    break
                if taulell[fitxes[z][0] - j][fitxes[z][1] + j] == fitxa:
                    comptador += 1
                if comptador == calc:
                    if calc == 3:
                        if taulell[fitxes[z][0] - j][fitxes[z][1] + j + 1] != " ":
                            for i in range(4):
                                if taulell[fitxes[z][0] - i][fitxes[z][1] + i] == " ":
                                    return (fitxes[z][0] - i, fitxes[z][1] + i)
                        else:
                            return False
                    else:
                        return True
            '''
            Ordre de comprovció
            #
                #
                    ## 
            '''
            comptador = 0
            for j in range(4):
                if fitxes[z][0] - j < 0 or (fitxes[z][1] - j) < 0:
                    break
                if taulell[fitxes[z][0] - j][fitxes[z][1] - j] == fitxa:
                    comptador += 1
                if comptador == calc:
                    if calc == 3:
                        for i in range(4):
                            if taulell[fitxes[z][0] - i][fitxes[z][1] - i] == " ":
                                if taulell[fitxes[z][0] - i + 1][fitxes[z][1] - i] != " ":
                                    return (fitxes[z][0] - i, fitxes[z][1] - i)
                        else:
                            return False
                    else:
                        return True
            z += 1
            if z == len(taulell) and sw == 0 or sw == 5:
                sw = 1
                z = 0
                calc = 3
    return False


def marcar_jugada_guanyadora(taulell, jugada):
    fitxa = taulell[jugada[0]][jugada[1]]
    c = 0
    fitxes = []
    for i in range(-4, 4, 1):
        if jugada[0] + i > len(taulell) - 1 or jugada[0] + i < 0:
            continue
        if taulell[jugada[0] + i][jugada[1]] == fitxa:
            fitxes.append((jugada[0] + i, jugada[1]))
    for i in range(len(fitxes)):
        if i > len(fitxes)/2 - 3:
            break
        if fitxes[i][0] != fitxes[i+1][0]:
            break
        else:
            c += 1
    if c >= 4:
        for i in range(c):
            taulell[fitxes[0][0] + i][fitxes[0][1]] = fitxa.upper()
    #columnas
    c = 0
    for i in range(4):
        if jugada[0] + i > len(taulell) - 1:
            break
        if taulell[jugada[0] + i][jugada[1]] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] + i][jugada[1]] = fitxa.upper()
    c = 0
    fitxes = []
    for i in range(-4, 4, 1):
        if jugada[1] + i > len(taulell) - 1 or jugada[1] + i < 0:
            continue
        if taulell[jugada[0]][jugada[1] + i] == fitxa:
            fitxes.append((jugada[0], jugada[1] + i))
    for i in range(len(fitxes)):
        if i + 1> len(fitxes) - 1:
            break
        if fitxes[i][0] != fitxes[i + 1][0]:
            break
        else:
            c += 1
    if c >= 4:
        for i in range(c):
            taulell[fitxes[0][0] + i][fitxes[0][1]] = fitxa.upper()
    c = 0
    for i in range(-4, 4, 1):
        if jugada[1] + i > len(taulell) - 1 or jugada[1] + i < 0:
            continue
        if taulell[jugada[0]][jugada[1] + i] == fitxa:
            c += 1

    if c >= 4:
        for j in range(-3):
            taulell[jugada[0]][jugada[1] + j + i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] + i > len(taulell) - 1:
            break
        if taulell[jugada[0] + i][jugada[1]] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] + i][jugada[1]] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] - i < 0:
            break
        if taulell[jugada[0] - i][jugada[1]] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] - i][jugada[1]] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[1] + i > len(taulell[0]) - 1:
            break
        if taulell[jugada[0]][jugada[1] + i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0]][jugada[1] + i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[1] - i < 0:
            break
        if taulell[jugada[0]][jugada[1] - i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0]][jugada[1] - i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] + i > len(taulell) - 1 or jugada[1] - i < 0:
            break
        if taulell[jugada[0] + i][jugada[1] - i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] + i][jugada[1] - i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] - i < 0 or jugada[1] - i < 0:
            break
        if taulell[jugada[0] - i][jugada[1] - i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] - i][jugada[1] - i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] + i > len(taulell) - 1 or jugada[1] + i > len(taulell[0]) - 1:
            break
        if taulell[jugada[0] + i][jugada[1] + i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] + i][jugada[1] + i] = fitxa.upper()
    c = 0
    for i in range(4):
        if jugada[0] + i > len(taulell) - 1 or jugada[1] - i < 0:
            break
        if taulell[jugada[0] + i][jugada[1] - i] == fitxa:
            c += 1
    if c == 4:
        for i in range(4):
            taulell[jugada[0] + i][jugada[1] - i] = fitxa.upper()
    return taulell


def espai(taulell):
    for i in taulell:
        for j in i:
            if j == " ":
                return True
    return False