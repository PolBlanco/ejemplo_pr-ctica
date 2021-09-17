from conecta4 import *
from random import randint
def main():
    '''
    Conecta4.
    Només cal canviar aquí les files i columnes del taulell perque es faci efectiu el canvi.
    Les fitxes de la màquina son O i les teves X.
    :return:
    '''
    files = 6
    columnes = 7
    '''jugador = [{"nom": input('Introdueix el teu nom: '), "partides": {"guanyades": 0, "perdudes": 0, "empatades": 0},
                "jugadespartidaka": []}, {"nom": "Màquina", "partides": {"guanyades": 0, "perdudes": 0, "empatades": 0},
                                          "jugadespartidaka": []}]'''
    jugador = [{"nom": "Màquina", "partides": {"guanyades": 0, "perdudes": 0, "empatades": 0}, "jugadespartidaka": []}]
    torn = randint(0,1)
    jugades = []
    while True:                     #sessió
        menu(jugador)
        noms = []
        juga = input("Introdueix el teu nom: ")
        for i in range(len(jugador)):
            noms.append(jugador[i]['nom'])
        if juga not in noms:
            jugador.append({"nom": juga, "partides": {"guanyades": 0, "perdudes": 0, "empatades": 0}, "jugadespartidaka": []})
        else:
            input("Benvingut de nou! Prem intro per continuar.")
        for i in range(len(jugador)):
            if jugador[i]['nom'] == juga:
                juga = i
                break
        taulell = crear_taulell(files, columnes)
        fitxes = [21, 21]
        while not guanyar(taulell, fitxa(not torn),1) and fitxes[torn] != 0 and espai(taulell):                 #partida
            mostrar_taulell(taulell, files, columnes, jugador, fitxes, juga, torn)
            jugada = fer_jugada(torn,columnes, taulell, files)
            fitxes[torn] -= 1
            taulell[jugada[0]][jugada[1]] = fitxa(torn)
            torn = not torn
            jugades.append(jugada)
        if guanyar(taulell, fitxa(not torn),1):
            taulell = marcar_jugada_guanyadora(taulell, jugada)
            mostrar_taulell(taulell, files, columnes, jugador, fitxes, juga, torn)
            if torn == False:
                print(f"Has guanyat {jugador[juga]['nom']}! I has utilitzat {21 - fitxes[torn]} fitxes!")
                jugador[juga]['partides']['guanyades'] += 1
                jugador[0]['partides']['perdudes'] += 1
                if len(jugades) < len(jugador[juga]["jugadespartidaka"]):
                    jugador[juga]["jugadespartidaka"].clear()
                    for i in jugades:
                        jugador[juga]["jugadespartidaka"].append(i)
            else:
                print(f"Ha guanyat la màquina! I ha utilitzat {21 - fitxes[torn]} fitxes!")
                jugador[0]['partides']['guanyades'] += 1
                jugador[juga]['partides']['perdudes'] += 1
                if len(jugades) < len(jugador[0]["jugadespartidaka"]):
                    jugador[0]["jugadespartidaka"].clear()
                    for i in jugades:
                        jugador[0]["jugadespartidaka"].append(i)
        else:
            jugador[juga]['partides']['empatades'] += 1
            jugador[0]['partides']['empatades'] += 1
            mostrar_taulell(taulell, files, columnes, jugador, fitxes, juga, torn)
            print(f"Heu empatat!")
        input()


if __name__ == '__main__':
    main()