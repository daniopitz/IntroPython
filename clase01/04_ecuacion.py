#casos de prueba a=1, b=3, c=2
from math import sqrt

a=int(input('Ingrese el valor de a'))
b=int(input('Ingrese el valor de b'))
c=int(input('Ingrese el valor de c'))



x1=(-b + sqrt(b**2-4*a*c))/2*a
x2=(-b - sqrt(b**2-4*a*c))/2*a


print(x1)
print(x2)
