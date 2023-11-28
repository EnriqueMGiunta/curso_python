signo = 1
entero = 0
entrada = 0
index = 0
while entrada != "":
    entrada = input(f"\nIngrese un valor: ")
    for char in entrada:
        if char == "-" and index != 0 or char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("No convertible a número")
            entero = NO
            break
        index +=1
if entero != "NO":
    entero = int(entrada)
print(f"Valor = {entero}, tipo = {type(entero)}")