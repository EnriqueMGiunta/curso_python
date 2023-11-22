# Simulador de cajero automático
# <enriquemgiunta@gmail.com>
#┌─┬─┐
#│ │ │
#├─┼─┤
#└─┴─┘

def menu_principal():
    seleccion = 0
    while seleccion <= 0 or seleccion > len(cuentas):
        titulo()
        print(f"{margen}  Cuentas disponibles:\n")
        for y in range(len(cuentas)):
            print(f"{margen}  {y + 1} - {cuentas[y][0]}")
        print(f"\n{margen}  9 - Salir.")
        seleccion = int(input(f"\n{margen}Elija con qué cuenta trabajar (1 - {y + 1}): "))
        if seleccion != 99:
            print(f"{margen}Cuenta seleccionada: {cuentas[seleccion - 1][0]}\n")
    return seleccion - 1

def titulo():
    
    print(f"{margen}┌────────────────────────────┐")
    print(f"{margen}│  CAJERO AUTOMÁTICO VIRTUAL │")
    print(f"{margen}└────────────────────────────┘")
    return

def titulo_cuenta(_cuenta):
    titulo()
    print(f"{margen}┌────────────────────────────┐")
    print(f"{margen}│   CUENTA: \"{cuentas[_cuenta][0]}\"")
    print(f"{margen}└────────────────────────────┘\n")
    return

def login(_cuenta):
    intentos = 3
    titulo_cuenta(_cuenta)
    while intentos >= 0:
        pw = input(f"\n{margen}   Ingrese su contraseña de acceso: ")    
        if pw != cuentas[_cuenta][1]:
            print(f"\n{margen}   Contraseña incorrecta, le quedan {intentos} intentos.")
            intentos -= 1
        else:
            return True
    return False

def consultar_saldo(_cuenta):
    titulo_cuenta(_cuenta)
    print(f"{margen}   El saldo de la cuenta es de ${cuentas[_cuenta][2]}.")
    input(f"\n{margen}   Pulse enter para volver al menú.")
    return

def ingresar_dinero(_cuenta):
    titulo_cuenta(_cuenta)
    monto = -1
    type(monto)
    while monto < 0 or type(monto) != int:
        monto = int(input(f"\n{margen}   Cantidad de pesos argentinos (AR$) a ingresar? (0 para salir): "))
        if monto == 0:
            return False
        elif monto < 0:
            print(f"{margen}   El monto no puede ser negativo.")
        elif type(monto) != "int":
            print(f"{margen}   El monto debe ser un número.")
    cuentas[_cuenta][2] += monto
    print(f"\n{margen}   Se ingresó la suma de ${monto} a la cuenta \"{cuentas[_cuenta][0]}\".")
    print(f"\n{margen}   El nuevo saldo es de ${cuentas[_cuenta][2]}.")
    return True

def menu_cuenta(_cuenta):
    operacion = 0
    while operacion != 9:
        titulo_cuenta(_cuenta)
        print(f"{margen}   1 - Consultar saldo.")
        print(f"{margen}   2 - Ingresar dinero.")
        print(f"{margen}   3 - Retirar dinero.")
        print(f"{margen}   4 - Transferir dinero.")
        print(f"{margen}   9 - Salir.")
        operacion = int(input(f"\n{margen}Elija una opción."))
        if operacion == 1:
            consultar_saldo(_cuenta)
        elif operacion == 2:
            cuentas[_cuenta][2] += ingresar_dinero(_cuenta)
    return

# *************** Bloque principal *****************
from os import system
cuentas = [
        ["Mario", "Paasswwoorrddsss", 300000],
        ["Raquel", "Otra_clave", 320000],
        ["Camila", "Ad1v1n4", 45000],
        ["Sol", "Malbec", 5000]
        ]
salir = False
margen = "          "

test = cuentas[0][1]
tb = ""
for c in test:
    print(c)
    tb = tb + (c or 127)
print(test,tb)
print(test, end="\r")

cuenta_elegida = menu_principal()
while cuenta_elegida != 8:
    if login(cuenta_elegida):
        menu_cuenta(cuenta_elegida)
        menu_principal()
print(f"{margen}Gracias por usar Cajero Virtual.")
