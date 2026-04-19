N=3
i=0
contador=0
suma_grande=0
while i<N:
    gasto=int(input('Ingrese gasto del dia: '))
    if gasto >=20000:
        suma_grande=suma_grande+gasto
        contador=contador+1 #contamos solo gastos grandes
    i=i+1 

print('Total',suma_grande)
print('Numero de gastos',contador)
