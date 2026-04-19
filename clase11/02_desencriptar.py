palabra='01nd9'
clave='murcielago'
palabra_nueva=''
for letra in palabra:
    if letra in '1234567890':
        palabra_nueva+=clave[int(letra)]
    else:
        palabra_nueva+=letra

print(palabra_nueva)
        
        
