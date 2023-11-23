# TA TE TI
def jugada_maquina():
    siguiente = False
    trio = []
    trio_x1 = []
    trio_x2 = []
    prioridad_1.clear()
    prioridad_2.clear()
    prioridad_3.clear()
    # Separa en tríos horizontales y diagonales, y analiza.
    for a in range(3):
        analizar(tablero[a])
        trio_x1.append(tablero[a][a])
        trio_x2.append(tablero[a][2-a])
    analizar(trio_x1)
    analizar(trio_x2)
    # Separa en tríos verticales y analiza.
    for x in range(3):
        for y in range(3):
            trio.append(tablero[y][x])
        analizar(trio)
        trio.clear()
    # Selecciona de entre las mejores opciones.
    while siguiente == False:
        if len(prioridad_1) != 0:
            pos_maquina = str(prioridad_1[int(randint(0, len(prioridad_1) - 1))])
        elif len(prioridad_2) != 0:
            pos_maquina = str(prioridad_2[int(randint(0, len(prioridad_2) - 1))])
        elif len(prioridad_3) != 0:
            pos_maquina = str(prioridad_3[int(randint(0, len(prioridad_3) - 1))])
        else:
            pos_maquina = str(randint(0, 9))
        #Coloca la ficha.
        print(f"Jugada máquina = \"{pos_maquina}\"")
        if coloca_ficha(pos_maquina, ficha_maquina):
            siguiente = True
    return

def analizar(_trio):
    # Analiza si ese trío está casi completo por la máqquina y selecciona la posición restante.
    if _trio.count(ficha_maquina) == 2 and _trio.count(ficha_humano) == 0:
        for elemento in _trio:
            if elemento != ficha_maquina and elemento != ficha_humano:
                if elemento not in prioridad_1:
                    prioridad_1.append(elemento)
    # Analiza si ese trío está casi completo por el humano y selecciona la posición restante.
    if _trio.count(ficha_humano) == 2 and _trio.count(ficha_maquina) == 0:
        for elemento in _trio:
            if elemento != ficha_maquina and elemento != ficha_humano:
                if elemento not in prioridad_2:
                    prioridad_2.append(elemento)
    # Analiza si ese trío tiene al menos 1 ficha y determina posiciones a usar.
    if _trio.count(ficha_maquina) == 1 and _trio.count(ficha_humano) == 0:
        for elemento in _trio:
            if elemento != ficha_maquina and elemento != ficha_humano:
                if elemento not in prioridad_3:
                    prioridad_3.append(elemento)
    print(f"Trio analizado: {_trio}     Prioridad 1 = {prioridad_1}     Prioridad 2 = {prioridad_2}     Prioridad 3 = {prioridad_3}")
    return

def jugada_humano():
    siguiente = False
    while siguiente == False:
        pos_humano = input("Ingrese el número de casillero donde colocar su jugada: (1 - 9)")
        if pos_humano in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if coloca_ficha(pos_humano, ficha_humano):
                siguiente = True
                cls()
        else:
            print("Ingrese un número del 1 al 9:")
    return

def coloca_ficha(_pos, _ficha):    
    salida = False
    for y in range(3):
        for x in range(3):
            if _pos == tablero[y][x]:
                tablero[y][x] = _ficha
                #dibuja_tablero()
                salida = True
                break
    return salida    

def dibuja_tablero():
    # Diccionario de colores
    gris = "\033[97m"
    verde = "\033[92m"
    rojo = "\033[91m"
    amarillo = "\033[93m"
    azul = "\033[94m"
    rosa = "\033[95m"
    oscuro = "\033[90m"
    # Dibuja el tablero con colores.
    normal = gris
    base = amarillo
    grilla = verde
    print(f"\n\nTa Te Ti (Ver 2.0 - Enrique Giunta)\n")
    print(f"{grilla}┌───┬───┬───┐")
    print(f"│ {base}{tablero[0][0]} {grilla}│ {base}{tablero[0][1]} {grilla}│ {base}{tablero[0][2]} {grilla}│")
    print("├───┼───┼───┤")
    print(f"│ {base}{tablero[1][0]} {grilla}│ {base}{tablero[1][1]} {grilla}│ {base}{tablero[1][2]} {grilla}│")
    print("├───┼───┼───┤")
    print(f"│ {base}{tablero[2][0]} {grilla}│ {base}{tablero[2][1]} {grilla}│ {base}{tablero[2][2]} {grilla}│")
    print(f"└───┴───┴───┘{normal}")

def revisa_estado():
    ganador = " "
    for ficha in ["x", "o"]:
        for x in range(3):
            if ficha == tablero[0][x] and ficha == tablero[1][x] and ficha == tablero[2][x]:
                ganador = ficha
            elif ficha == tablero[x][0] and ficha == tablero[x][1] and ficha == tablero[x][2]:
                ganador = ficha
        if ficha == tablero[0][0] and ficha == tablero[1][1] and ficha == tablero[2][2]:
            ganador = ficha
        if ficha == tablero[2][0] and ficha == tablero[1][1] and ficha == tablero[0][2]:
            ganador = ficha
    return ganador

def cls():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    return



# ******* Bloque principal ********
from random import randint
import os
prioridad_1 = []
prioridad_2 = []
prioridad_3 = []
nuevo_juego = "s"
ficha_por_omision = "x"
while nuevo_juego == "s":
    tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    gano = "."
    jugada = 0
    orden = randint(0, 1)

    cls()
    dibuja_tablero()
    ficha_humano = input(f"Elija su ficha \"o\" \"x\" ({ficha_por_omision}):")
    if ficha_humano != "x" and ficha_humano != "o":
        ficha_humano = ficha_por_omision
    if ficha_humano == "x":
        ficha_maquina = "o"
    else:
        ficha_maquina = "x"
    ficha_por_omision = ficha_humano
    while gano != "o" and gano != "x" and jugada < 9:
        dibuja_tablero()
        if (jugada + orden)%2 == 0:
            jugada_humano()
            gano = revisa_estado()
        else:
            jugada_maquina()
            gano = revisa_estado()
        jugada += 1
    dibuja_tablero()
    if gano == ficha_humano:
        print(f"\nGanador: \"EL HUMANO\", felicitaciones!!!")
    elif gano == ficha_maquina:
        print(f"\nGanador: \"LA COMPUTADORA\", felicitaciones a mí!!!")
    else:
        print(f"\nEMPATE.")
    
    nuevo_juego = input(f"Jugamos de nuevo \"s\" \"n\" (s)? ")
    if nuevo_juego != "n":
        nuevo_juego = "s"