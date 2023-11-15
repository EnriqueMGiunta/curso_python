# TA TE TI
def jugada_maquina():
    pass

def jugada_humano():
    siguiente = False
    while siguiente == False:
        pos_humano = input("Ingrese el número de casillero donde colocar su jugada: (1 - 9)")
        if pos_humano in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if coloca_ficha(pos_humano, ficha_humano):
                siguiente = True
        else:
            print("Ingrese un número del 1 al 9.")

def coloca_ficha(_pos, _ficha):    
    salida = False
    for y in range(3):
        for x in range(3):
            print(f"tablero[{y}][{x}] tiene {tablero[y][x]} = {_pos} ?")
            if _pos == tablero[y][x]:
                tablero[y][x] = _ficha
                salida = True
                break
    print(f"Salida al colocar ficha={salida}")
    dibuja_tablero()
    return salida    
    
def dibuja_tablero():
    print("┌───┬───┬───┐")
    print(f"│ {tablero[0][0]} │ {tablero[0][1]} │ {tablero[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tablero[1][0]} │ {tablero[1][1]} │ {tablero[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tablero[2][0]} │ {tablero[2][1]} │ {tablero[2][2]} │")
    print("└───┴───┴───┘")

def revisa_estado(_jugador):
    ganador = " "
    for x in range(3):
        if _jugador == tablero[0][x] and _jugador == tablero[1][x] and _jugador == tablero[2][x]:
            ganador = _jugador
        elif _jugador == tablero[x][0] and _jugador == tablero[x][1] and _jugador == tablero[x][2]:
            ganador = _jugador
    if _jugador == tablero[0][0] and _jugador == tablero[1][1] and _jugador == tablero[2][2]:
        ganador = _jugador
    if _jugador == tablero[2][0] and _jugador == tablero[1][1] and _jugador == tablero[0][2]:
        ganador = _jugador
    return ganador

from random import randint
tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
gano = "."
numero_aleatorio = randint(0, 18)
print("Ta Te Ti")
ficha_humano = input("Elija un símbolo para su jugador (x o):")
if ficha_humano == "x":
    ficha_maquina = "o"
else:
    ficha_maquina = "x"
orden = randint(1, 2)
while(gano != "o" and gano != "x"):
    dibuja_tablero()
    if orden == 1:
        jugada_humano()
        jugada_maquina()
    else:
        jugada_maquina()
        jugada_humano()
