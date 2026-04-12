condicion1=False

while condicion1==False:
    caracter=input('Ingrese caracter:')
    if caracter == '#':
        condicion1=True

condicion2=False

while condicion2==False:
    ancho=int(input('Ingrese ancho: '))
    alto=int(input('Ingrese alto: '))
    if (ancho > 2) and (alto >2):
        condicion2=True

if (condicion1== True) and (condicion2==True):
    h=0
    espacio=' '
    print(ancho*caracter)
    while h<alto-2:
        print(caracter+espacio*(ancho-2)+caracter)
        h=h+1
    print(ancho*caracter)

