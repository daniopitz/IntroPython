n=int(input('Ingrese numero de estudiantes: '))
i=0
while i<n:
    print('Estudiante:', i+1)
    j=0
    suma=0
    while j<3:
        nota=float(input('Ingrese nota: '))
        print('Nota', j+1, ':', nota)
        suma=suma+nota
        j=j+1
    print('Promedio:', round(suma/3,1))
    i=i+1
    print()



                   
