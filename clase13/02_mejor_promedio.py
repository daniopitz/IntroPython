def encontrar(texto, caracter):
    posicion = 0
    for c in texto:
        if c == caracter:
            return posicion
        posicion = posicion + 1
    return -1


def promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def maximo(a, b):
    if a >= b:
        return a
    else:
        return b


# Programa principal
nombre1 = input("Nombre del estudiante 1: ")
notas1 = input("Notas de " + nombre1 + " (separadas por coma): ")

pos1 = encontrar(notas1, ",")
nota1_a = float(notas1[:pos1])
resto1 = notas1[pos1+1:]
pos1b = encontrar(resto1, ",")
nota1_b = float(resto1[:pos1b])
nota1_c = float(resto1[pos1b+1:])
prom1 = promedio(nota1_a, nota1_b, nota1_c)

nombre2 = input("Nombre del estudiante 2: ")
notas2 = input("Notas de " + nombre2 + " (separadas por coma): ")

pos2 = encontrar(notas2, ",")
nota2_a = float(notas2[:pos2])
resto2 = notas2[pos2+1:]
pos2b = encontrar(resto2, ",")
nota2_b = float(resto2[:pos2b])
nota2_c = float(resto2[pos2b+1:])
prom2 = promedio(nota2_a, nota2_b, nota2_c)

mejor = maximo(prom1, prom2)

print()
if mejor == prom1:
    print("El mejor promedio lo obtuvo", nombre1, "con", round(prom1, 2))
else:
    print("El mejor promedio lo obtuvo", nombre2, "con", round(prom2, 2))
