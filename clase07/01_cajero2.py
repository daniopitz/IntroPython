contraseña = input('Ingrese contraseña: ')
intentos = 1

while contraseña != '1234' and intentos < 3:
    print('Contraseña incorrecta, intente de nuevo.')
    contraseña = input('Ingrese contraseña: ')
    intentos = intentos + 1

if contraseña == '1234':
    print('Acceso permitido')
else:
    print('Acceso denegado. Demasiados intentos')
