def clave_correcta(clave):
    if clave == "python2025":
        return True
    else:
        return False


# Programa principal
intentos = 0
acerto = False

while intentos < 3 and  acerto==False:
    clave = input("Ingrese su clave: ")
    intentos = intentos + 1
    if clave_correcta(clave):
        acerto = True

if acerto==True:
    print("Acceso concedido en el intento", intentos)
else:
    print("Cuenta bloqueada")
