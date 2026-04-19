#Sumo numeros desde 1 a 3
n = int(input("Ingrese un numero: "))

suma = 0 #acumulador

contador = 0 #contador

while contador <= n:
  suma += contador
  contador += 1

print('Suma', suma)
