filas = int(input("Ingrese filas: "))
columnas = int(input("Ingrese columnas: "))

i = 0
while i < filas:
    j = 0
    while j < columnas:
        print("X", end=" ")
        j = j + 1
    print()
    i = i + 1


