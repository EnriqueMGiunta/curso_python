# Simulador de cajero automático
# <enriquemgiunta@gmail.com>
#┌─┬─┐
#│ │ │
#├─┼─┤
#└─┴─┘

def menu_principal():
    seleccion = -1
    while type(seleccion) != int or seleccion < 0 or seleccion > len(cuentas) - 1:
        titulo()
        print(f"{margen}  Cuentas disponibles:\n")
        for y in range(len(cuentas)):
            print(f"{margen}  {y} - {cuentas[y][0]}")
        print(f"\n{margen}  99 - Salir.")
        seleccion = opcion(f"Elija con qué cuenta trabajar (0 - {y}): ", 0, len(cuentas) - 1, 99)
        if seleccion == 99:
            return 99
    print(f"{margen}Cuenta seleccionada: {cuentas[seleccion][0]}\n")
    return seleccion

def titulo():
    cls()
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

def opcion(_texto, _ini, _fin, _salida):
    """
    Pide ingresar un valor mostrando el texto: _texto
    Chequea que lo ingresado esté entre _ini y _fin.
    Si lo ingresado es igual a _salida o está entre :ini y _fin, retorna con ese valor.

    Args:
        _texto (_str_): Texto a mostrar para ingreso de un valor.
        _ini (_int_): Valor entero inicial del rango de opciones permitidas.
        _fin (_int_): Valor entero final del rango de opciones permnitidas.
        _salida (_int_): Valor entero extra usado como valor de salida del menú.

    Retorna:
        Valor ingresado válido.
    """
    entero = "no_verificado"
    signo = 1
    # Determina si el valor ingresado puede hacerse entero.
    while entero in ["no_verificado", "error"] or salida == "error":
        entrada = input(f"{margen}{_texto} ")
        if entrada == "":
            return _salida
        if entrada[0] == "-":
            signo = -1
            entrada[0] = 0
        for char in entrada:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                entero = "error"
                break
        entero = signo * int(entrada)
        # Determina si el entero está dentro de las opciones.
        if entero != _salida and entero not in range(_ini, _fin + 1):
            print(f"{margen}El valor ingresado no está entre las opciones.")
            salida = "error"
        else:
            salida = entero
    return salida

def login(_cuenta):
    intentos = 3
    titulo_cuenta(_cuenta)
    while intentos >= 0:
        pw = input(f"\n{margen}Ingrese su contraseña de acceso: ")    
        if pw != cuentas[_cuenta][1]:
            print(f"\n{margen}Contraseña incorrecta, le quedan {intentos} intentos.")
            intentos -= 1
        else:
            return True
    return False

def consultar_saldo(_cuenta):
    titulo_cuenta(_cuenta)
    print(f"{margen}El saldo de la cuenta es de ${cuentas[_cuenta][2]}.")
    input(f"{margen}Pulse enter para volver al menú.")
    return

def ingresar_dinero(_cuenta):
    titulo_cuenta(_cuenta)
    monto = -1
    while monto < 0 or type(monto) != int or monto%100 != 0:
        monto = opcion(f"\n{margen} Indique la cantidad de pesos argentinos (AR$) a ingresar, en múltiplos de 100. (0 para salir):\n{margen}", -999999999999999999, 999999999999999999, 0)
        if monto == 0:
            return False
        elif monto < 0:
            print(f"{margen}El monto no puede ser negativo.")
        elif monto%100 != 0:
            print(f"{margen}El monto debe ser múltiplo de 100.")
        elif type(monto) != int:
            print(f"{margen}El monto debe ser un número.")
    return monto

def retirar_dinero(_cuenta):
    monto = -1
    while monto < 0 or type(monto) != int or monto%100 != 0:
        monto = opcion(f"\n{margen} Indique la suma de pesos argentinos (AR$) a retirar, en múltiplos de 100. (0 para salir):\n{margen}", -999999999999999999, 999999999999999999, 0)
        if monto == 0:
            return False
        elif monto < 0:
            print(f"{margen}El monto no puede ser negativo.")
        elif monto%100 != 0:
            print(f"{margen}El monto debe ser múltiplo de 100.")
        elif type(monto) != int:
            print(f"{margen}El monto debe ser un número.")
    return monto

def menu_cuenta(_cuenta):
    operacion = 0
    while operacion != 9:
        titulo_cuenta(_cuenta)
        print(f"{margen}   1 - Consultar saldo.")
        print(f"{margen}   2 - Ingresar dinero.")
        print(f"{margen}   3 - Retirar dinero.")
        print(f"{margen}   4 - Transferir dinero.\n")
        print(f"{margen}   9 - Salir.")
        operacion = opcion(f"\n{margen}Elija una opción.", 1, 4, 9)
        if operacion == 1:
            consultar_saldo(_cuenta)
        elif operacion == 2:
            ingreso = ingresar_dinero(_cuenta)
            cuentas[_cuenta][2] += ingreso
            print(f"\n{margen}{rojo}Por favor coloque los billetes.{gris}")
            input(f"{margen}Enter para continuar.")
            print(f"\n{margen}Se ingresó la suma de ${ingreso} a la cuenta \"{cuentas[_cuenta][0]}\".")
            print(f"\n{margen}El nuevo saldo es de ${cuentas[_cuenta][2]}.")
            input(f"{margen}Enter para continuar.")
        elif operacion == 3:
            retiro = retirar_dinero(_cuenta)
            while retiro > cuentas[_cuenta][2]:
                print(f"{margen}No se puede retirar más dinero del disponible en su cuenta.")
                print(f"{margen}Máximo: ${cuentas[_cuenta][2]}")
                retiro = retirar_dinero(_cuenta)
            else:
                cuentas[_cuenta][2] -= retiro
                print(f"\n{margen}Se extrajo la suma de ${retiro} de la cuenta \"{cuentas[_cuenta][0]}\".")
                print(f"\n{margen}El nuevo saldo es de ${cuentas[_cuenta][2]}.")
                print(f"\n{margen}{rojo}Por favor retire los billetes.{gris}")
            input(f"{margen}Enter para continuar.")
    return

def cls():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    return



# *************** Bloque principal *****************
import os
cuentas = [
        ["Mario", "Paasswwoorrddsss", 300000],
        ["Raquel", "Otra_clave", 320000],
        ["Camila", "Ad1v1n4", 45000],
        ["Sol", "Malbec", 5000]
        ]
salir = False
margen = "          "
# Diccionario de colores
gris = "\033[97m"
verde = "\033[92m"
rojo = "\033[91m"
amarillo = "\033[93m"
azul = "\033[94m"
rosa = "\033[95m"
oscuro = "\033[90m"
test = cuentas[0][1]
tb = ""
for c in test:
    print(c)
    tb = tb + (c or 127)
print(test,tb)
print(test, end="\r")

while salir == False:
    cuenta_elegida = menu_principal()
    if cuenta_elegida == 99:
        salir = True
    elif login(cuenta_elegida):
        menu_cuenta(cuenta_elegida)
print(f"{margen}Gracias por usar Cajero Virtual.")

