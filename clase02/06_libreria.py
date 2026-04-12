#Alternativa 1
n_libros=int(input('Ingrese cantidad de libros a combrar:'))


if n_libros >3:
    print('Descuento aplicado')
    print('Precio a pagar:', 12000*n_libros*0.9)

else:
    print('Precio a pagar:', 12000*n_libros)


#Alternativa 2


n_libros=int(input('Ingrese cantidad de libros a combrar:'))


if n_libros >3:
    print('Descuento aplicado')
    p=n_libros*1200*0.9

else:
    p=n_libros*1200
print(p)



    
                

             
