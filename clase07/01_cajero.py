acceso=False
intentos=0
while intentos <3 and acceso==False:
    contraseña=input('Ingrese contraseña: ')
    intentos=intentos + 1
    if contraseña=='1234':
        print('Acceso permitido: ')
        acceso=True

if intentos>=3:
    print ('Acceso denegado. Demadiaso intentos')
        
        
    
