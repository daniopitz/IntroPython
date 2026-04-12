import math

x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))
x3 = float(input("Ingrese x3: "))
y3 = float(input("Ingrese y3: "))

lado1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
lado2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
lado3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

perimetro = lado1 + lado2 + lado3

print("El perimetro del triangulo es:", perimetro)
