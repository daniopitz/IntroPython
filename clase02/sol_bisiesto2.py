#Solución 
#Es bisiesto si es divisible por 400 o
#es divisible por 4 pero no por 100

a=int(input("Ingresa año: "))

if(a % 4 == 0 and a % 100 != 0):
	print("El año "+str(a)+ " si es bisiesto")

elif a % 400 == 0:
	print("El año "+str(a)+ " si es bisiesto")

else:
	print("El año "+str(a)+ " no es bisiesto")
    