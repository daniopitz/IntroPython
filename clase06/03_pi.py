k=0
suma=0
a=True

while a==True:
    serie=(-1)**k/(2*k+1)
    suma+=serie
    if abs(serie) <=10**(-5):
        a=False

    k=k+1
print('Valor de pi',4*suma)
