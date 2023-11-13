# TA TE TI
def jugada_maquina():
    pass

def jugada_humano():
    pos_humano = "."
    while pos_humano not in tablero:
        pos_humano = input("Ingrese la posición dónde colocar su jugada: (1 - 9)")
        if pos_humano < "1" or pos_humano > "9":
            print("Debe ingresar un valor entre 1 y 9.")
    print(f"índice de la posición es: {tablero.index(pos_humano)}")
    tablero[tablero.index(pos_humano)] = ficha_humano
    dibuja_tablero()
    revisa_estado()
    
def dibuja_tablero():
    print("     A   B   C ")
    print("   -------------")
    print(f"1  I {tablero[0,0]} I {tablero[0,1]} I {tablero[0,2]} I")
    print("   -------------")
    print(f"2  I {tablero[1,0]} I {tablero[1,1]} I {tablero[1,2]} I")
    print("   -------------")
    print(f"3  I {tablero[2,0]} I {tablero[2,1]} I {tablero[2,2]} I")
    print("   -------------")

def revisa_estado(_jugador):
    ganador = " "
    for x in range(3):
        if _jugador == tablero[0, x] and _jugador == tablero[1, x] and _jugador == tablero[2, x]:
            ganador = _jugador
        elif _jugador == tablero[x, 0] and _jugador == tablero[x, 1] and _jugador == tablero[x, 2]:
            ganador = _jugador
    if _jugador == tablero[0, 0] and _jugador == tablero[1, 1] and _jugador == tablero[2, 2]:
        ganador = _jugador
    if _jugador == tablero[2, 0] and _jugador == tablero[1, 1] and _jugador == tablero[0, 2]:
        ganador = _jugador
    return ganador

from random import randint
tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
gano = "."
numero_aleatorio = randint(0, 18)
print("Ta Te Ti")
ficha_humano = input("Elija un símbolo para su jugador (x o):")
while(gano != "o" and gano != "x"):
    dibuja_tablero()
    jugada_humano()
    jugada_maquina()
