from math import sqrt

a=float(input('Ingrese valor de a: '))
b=float(input('Ingrese valor de b: '))
c=float(input('Ingrese valor de c:'))

d=b**2-4*a*c

print('Discrimante: ', d)

if b**2 >=4*a*c:
        
x1=(-b + sqrt(b**2-4*a*c))/2*a
x2=(-b - sqrt(b**2-4*a*c))/2*a
print('x1: ', round(x1,2))
print('x2: ', round(x2,2))

else:
    print('La ecuacion no tiene solucion en los reales')
