año=int(input('Ingrese año: '))

bisiesto=año%400==0 or (año%4==0 and año%100!=0)

if bisiesto==True:
    print('El año es bisiesto')

else:
    print('El año no es bisiesto')
