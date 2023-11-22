# Simulador de cajero automático
# <enriquemgiunta@gmail.com>
def menu_principal():
    seleccion = 0
    while seleccion <= 0 or seleccion >= len(cuentas):
        num = 0
        print(f"""
            CAJERO AUTOMÁTICO VIRTUAL

            Cuentas disponibles:""")
        for cue in cuentas:
            num += 1
            print(f"    {num} - {cue}")
        seleccion = int(input(f"\nElija con qué cuenta trabajar: (1 - {len(cuentas)})"))
    return seleccion - 1


def login(_usuario):
    pass


# *************** Bloque principal *****************
cuentas = {"Mario": "Paasswwoorrddss", "Raquel": "Otra_clave", "Camila": "Ad1v1n4"}
cuenta_elegida = menu_principal()
print(cuentas["Camila"])
print(f"Cuenta seleccionada: {cuenta_elegida}")
#login(cuenta_elegida)

