# TA TE TI
def jugada_maquina():
    siguiente = False
    while siguiente == False:
        pos_maquina = str(randint(1, 9))
        print(f"Jugada máquina = \"{pos_maquina}\"")
        if coloca_ficha(pos_maquina, ficha_maquina):
            siguiente = True
    return

def jugada_humano():
    siguiente = False
    while siguiente == False:
        pos_humano = input("Ingrese el número de casillero donde colocar su jugada: (1 - 9)")
        if pos_humano in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if coloca_ficha(pos_humano, ficha_humano):
                siguiente = True
        else:
            print("Ingrese un número del 1 al 9.")
    return

def coloca_ficha(_pos, _ficha):    
    salida = False
    for y in range(3):
        for x in range(3):
            if _pos == tablero[y][x]:
                tablero[y][x] = _ficha
                dibuja_tablero()
                salida = True
                break
    return salida    

def dibuja_tablero():
    print("┌───┬───┬───┐")
    print(f"│ {tablero[0][0]} │ {tablero[0][1]} │ {tablero[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tablero[1][0]} │ {tablero[1][1]} │ {tablero[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tablero[2][0]} │ {tablero[2][1]} │ {tablero[2][2]} │")
    print("└───┴───┴───┘")

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


# ******* Bloque principal ********
from random import randint
nuevo_juego = "s"
ficha_por_omision = "x"
while nuevo_juego == "s":
    tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    gano = "."
    jugada = 0
    orden = randint(0, 1)

    print("\n\n\nTa Te Ti")
    ficha_humano = input(f"Elija un símbolo para su jugador \"o\" o \"x\" ({ficha_por_omision}):")
    if ficha_humano != "x" and ficha_humano != "o":
        ficha_humano = ficha_por_omision
    if ficha_humano == "x":
        ficha_maquina = "o"
    else:
        ficha_maquina = "x"
    ficha_por_omision = ficha_humano
    while gano != "o" and gano != "x" and jugada < 8:
        dibuja_tablero()
        if (jugada + orden)%2 == 0:
            jugada_humano()
            gano = revisa_estado()
        else:
            jugada_maquina()
            gano = revisa_estado()
        jugada += 1

    if gano == ficha_humano:
        print(f"\nGanador: \"EL HUMANO\", felicitaciones!!!\n\n")
    elif gano == ficha_maquina:
        print(f"\nGanador: \"LA COMPUTADORA\", felicitaciones a mí!!!\n\n")
    else:
        print(f"\nEsto fue un empate.\n\n")
    nuevo_juego = input(f"\nJugamos de nuevo (s / n)? ")
