import math

x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia es:", distancia)
