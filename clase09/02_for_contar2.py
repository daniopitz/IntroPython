texto=input('Ingrese texto: ')

contador=0
for letra in texto:
    if letra in 'aeiou':
        print(letra)
        contador+=1

print(contador)
        
