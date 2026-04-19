N=3
i=1
suma=0
contador=0
while i <=N:
    gasto=int(input('Ingrese gasto: '))
    if gasto >=20000:
        print('Gasto importante')
        suma=suma+gasto
        contador=contador+1
    i+=1
print('Suma gastos importantes', suma)
print('Numero gastos importantes',contador)
