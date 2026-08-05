def anios_para_votar(edad):
    if edad >= 18:
        return 0
    
    else:
        return 18 - edad


# Programa principal
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

faltan = anios_para_votar(edad)

if faltan == 0:
    print(nombre, "ya puede votar")
else:
    print("A", nombre, "le faltan", faltan, "años para votar")
