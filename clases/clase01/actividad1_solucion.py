a=int(input('Ingrese a:'))
b=int(input('Ingrese b:'))
c=int(input('Ingrese c:'))

x1=(-b+sqrt(b**2-4*a*c))/(2*a)
x2=(-b-sqrt(b**2-4*a*c))/(2*a)

print(x1, x2)