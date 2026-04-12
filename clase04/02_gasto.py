gasto=float(input('Ingrese gasto:'))


if gasto > 100:
    print('Debe pagar', gasto*0.8)
elif gasto >50:
    print('Debe pagar', gasto*0.9)

else:
    print('Debe pagar', gasto)
