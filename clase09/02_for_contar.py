texto=input('Ingrese texto: ')

contador=0
for letra in texto:
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        print(letra)
        contador+=1

print(contador)
        
