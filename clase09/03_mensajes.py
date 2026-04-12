mensaje = "Hola"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"

contador_may = 0
contador_min = 0

for letra in mensaje:
    if letra in mayusculas:
        contador_may+=1
    elif letra in minusculas:   # solo cuenta si realmente es minúscula
        contador_min += 1
    # si es espacio, número u otro no hace nada
        
if contador_may > contador_min:
    print('MODO ENOJADO')
else: 
    print('mensaje normal')
