a=True
while a==True:
    contraseña=input('Ingrese contraseña: ')
    if contraseña=='segura123':
        print('Acceso concedido')
        a=False
    else:
        print('Contraseña incorrecta, por favor vuelva a intentarlo')
    
