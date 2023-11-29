"""
Cajero automático Virtual. Ver 2.0
<enriquemgiunta@gmail.com>
"""
def cls():
    """ Limpia pantalla. """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    return

def titulo():
    """ Muestra la cabecera del cajero. """
    cls()
    print(f"{margen}┌────────────────────────────┐")
    print(f"{margen}│  CAJERO AUTOMÁTICO VIRTUAL │")
    print(f"{margen}└────────────────────────────┘")
    return

def titulo_cuenta(_cuenta):
    """ Muestra el título de la cuenta. """
    titulo()
    print(f"{margen}┌────────────────────────────┐")
    print(f"{margen}│   Bienvenido/a \"{cuentas[_cuenta][0]}\"", end="")
    print(" " * (9 - len(cuentas[_cuenta][0])), "│")
    print(f"{margen}└────────────────────────────┘\n\n")
    return

def menu_principal():
    """ Muestra el menú principal con las opciones disponibles. """
    seleccion = -1
    while type(seleccion) != int or seleccion < 0 or seleccion > len(cuentas) - 1:
        titulo()
        print(f"{margen}  Cuentas disponibles:\n")
        for y in range(len(cuentas)):
            print(f"{margen}  {y} - {cuentas[y][0]}")
        print(f"\n{margen}  99 - Salir.\n\n")
        seleccion = opcion(f"{margen} Elija con qué cuenta trabajar (0 - {y}): ", 0, len(cuentas) - 1, 99)
        if seleccion == 99:
            return 99
    return seleccion

def menu_cuenta(_cuenta):
    """ Muestra el menú de la cuenta. """
    operacion = 0
    titulo_cuenta(_cuenta)
    print(f"{margen}   1 - Consultar saldo.")
    print(f"{margen}   2 - Ingresar dinero.")
    print(f"{margen}   3 - Retirar dinero.")
    print(f"{margen}   4 - Transferir dinero.\n")
    print(f"{margen}   9 o Enter - Salir.\n\n")
    operacion = opcion(f"{margen} Elija una opción.", 1, 4, "9")
    return operacion

def opcion(_texto, _ini, _fin, _salida):
    """
    Pide ingresar un valor mostrando el texto: _texto
    Chequea que lo ingresado esté entre _ini y _fin.
    Si lo ingresado es igual a _salida o está entre _ini y _fin, retorna con ese valor.

    Args:
        _texto (_str_): Texto a mostrar para ingreso de un valor.
        _ini (_int_): Valor entero inicial del rango de opciones permitidas.
        _fin (_int_): Valor entero final del rango de opciones permnitidas.
        _salida (_int_): Valor entero extra usado como valor de salida del menú.

    Retorna:
        Valor ingresado válido.
    """
    # Determina si el valor ingresado puede hacerse entero.
    CURSOR_ARRIBA = '\x1b[1A'
    BORRA_LINEA = '\x1b[2K'
    _entero = "no_verificado"
    _retornar = "error"
    while _retornar == "error":
        while _entero == "no_convertible" or _entero == "no_verificado":
            _entrada = input(f"{CURSOR_ARRIBA}{BORRA_LINEA}{_texto} ")
            if _entrada == "":
                return _salida
            # Determina si el valor ingresado se puede convertir a entero sin tirar error.
            _entero = 0
            index = 0
            for char in _entrada:
                if (char == "-" and index != 0) or char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    _entero = "no_convertible"
                    break
                index += 1
        _entero = int(_entrada)
        # Determina si el entero está dentro de las opciones.
        if _entero != _salida and _entero not in range(_ini, _fin + 1):
            _retornar = "error"
            _entero = "no_verificado"
        else:
            _retornar = _entero
    return _retornar

def login(_cuenta):
    """ Pide la contraseña de acceso a la cuenta. """
    intentos = 3
    while intentos > 0:
        titulo_cuenta(_cuenta)
        pw = input(f"\n{margen} Ingrese su contraseña de acceso (tiene {intentos} reintentos): ")    
        if pw != cuentas[_cuenta][1]:
            intentos -= 1
        else:
            return True
    return False

def consultar_saldo(_cuenta):
    """ Consulta de saldo de la cuenta. """
    titulo_cuenta(_cuenta)
    print(f"{margen} El saldo de la cuenta es de ${cuentas[_cuenta][2]}.")
    input(f"{margen} Pulse enter para volver al menú anterior.")
    return

def ingresar_dinero(_cuenta):
    """ solicita los datos para ingresar dinero en la cuenta. """
    titulo_cuenta(_cuenta)
    monto = -1
    while monto < 0 or type(monto) != int or monto%100 != 0:
        monto = opcion(f"{margen} Indique la cantidad de pesos argentinos (AR$) a ingresar, en múltiplos de 100. Máximo $50.000 (0 para salir):\n{margen}", 100, 50000, 0)
        if monto < 0:
            print(f"{margen} El monto no puede ser negativo.")
        elif monto%100 != 0:
            print(f"{margen} El monto debe ser múltiplo de 100.")
        elif type(monto) != int:
            print(f"{margen} El monto debe ser un número.")
    return monto

def retirar_dinero(_cuenta):
    """ Solicita los datos para el retiro de dinero de la cuenta. """
    monto = -1
    while monto < 0 or type(monto) != int or monto%100 != 0:
        monto = opcion(f"{margen} Indique la suma de pesos argentinos (AR$) a retirar, en múltiplos de 100. Máximo $50.000 (0 para salir):\n{margen}", 0, 50000, 0)
        if monto == 0:
            return False
        elif monto < 0:
            print(f"{margen} El monto no puede ser negativo.")
        elif monto%100 != 0:
            print(f"{margen} El monto debe ser múltiplo de 100.")
        elif type(monto) != int:
            print(f"{margen} El monto debe ser un número.")
    return monto

def transferir_dinero():
    """Solicita los datos para transferir dinero a otra cuenta. """
    _monto  = 0
    _destino = 99
    _monto = opcion(f"{margen} Indique monto a transferir, dispone de ${cuentas[cuenta_elegida][2]}. (0 para salir): ", 1, cuentas[cuenta_elegida][2], 0)
    if _monto <= 0:
        return (0, 99)
    titulo()
    print(f"{margen}  Cuentas disponibles:\n")
    for y in range(len(cuentas)):
        print(f"{margen}  {y} - {cuentas[y][0]}")
    print(f"{margen}  ENTER ó 99 - Cancelar")
    _destino = opcion(f"\n{margen} Indique la cuenta de destino: ", 0, len(cuentas) - 1, 99)
    return (_monto, _destino)

"""
 **************************************************
 *************** BLOQUE PRINCIPAL *****************
 **************************************************
"""
import os
cuentas = [
        ["Mario", "clave1", 300000],
        ["Raquel", "clave2", 320000],
        ["Camila", "clave3", 45000],
        ["Alejanro", "clave4", 45000],
        ["Sol", "Malbec", 5000]
        ]
salir = False
salir_cuenta = False
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

while salir == False:
    cuenta_elegida = menu_principal()
    if cuenta_elegida == 99:
        salir = True
    elif login(cuenta_elegida):
        while salir_cuenta == False:
            operacion = menu_cuenta(cuenta_elegida)
            if operacion == 1:
                # Consulta de saldo
                consultar_saldo(cuenta_elegida)
            elif operacion == 2:
                # Ingresar dinero
                ingreso = ingresar_dinero(cuenta_elegida)
                if ingreso != 0:
                    cuentas[cuenta_elegida][2] += ingreso
                    print(f"\n{margen}{rojo} Por favor coloque los billetes y pulse enter para continuar.{gris}")
                    input("")
                    print(f"\n{margen} Se ingresó la suma de ${ingreso} a la cuenta \"{cuentas[cuenta_elegida][0]}\".")
                    print(f"\n{margen} El nuevo saldo es de ${cuentas[cuenta_elegida][2]}.")
                else:
                    print(f"\n{margen} Operación cancelada.")
                input(f"{margen} Enter para continuar.")
            elif operacion == 3:
                # Retirar dinero
                retiro = retirar_dinero(cuenta_elegida)
                while retiro > cuentas[cuenta_elegida][2]:
                    print(f"{margen} No se puede retirar más dinero del disponible en su cuenta.")
                    print(f"{margen} Máximo: ${cuentas[cuenta_elegida][2]}")
                    retiro = retirar_dinero(cuenta_elegida)
                if retiro == 0:
                    print(f"\n{margen} Operación cancelada.")
                else:
                    cuentas[cuenta_elegida][2] -= retiro
                    print(f"\n{margen} Se extrajo la suma de ${retiro} de la cuenta \"{cuentas[cuenta_elegida][0]}\".")
                    print(f"\n{margen} El nuevo saldo es de ${cuentas[cuenta_elegida][2]}.")
                    print(f"\n{margen}{rojo} Por favor retire los billetes.{gris}")
                input(f"{margen} Enter para continuar.")
            elif operacion == 4:
                # Transferir dinero
                transferencia, cuenta_destino = transferir_dinero()
                if cuenta_destino != 99:
                    cuentas[cuenta_elegida][2] -= transferencia
                    cuentas[cuenta_destino][2] += transferencia
                    print(f"\n{margen} Se transfirió la suma de ${transferencia} de la cuenta \"{cuentas[cuenta_elegida][0]}\" a la cuenta \"{cuentas[cuenta_destino][0]}\".")
                else:
                    print(f"\n{margen} Transferencia cancelada")
                input(f"{margen} Enter para continuar.")
            else:
                salir_cuenta = True
print(f"\n{margen}  Gracias por usar Cajero Virtual.")

