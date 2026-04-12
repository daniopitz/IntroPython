texto=input('Ingrese texto: ')
texto_nuevo=''
for letra in texto:
    if letra in 'aeiou':
        texto_nuevo+='*'
    else:
        texto_nuevo+=letra

print(texto_nuevo)
        
        
        
