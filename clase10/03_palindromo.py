texto = input('Ingrese palabra o frase:')
texto = texto.lower()

#quitar espacio
n = len(texto)
solo_letras = ''
for c in texto:
    if c != ' ':
        solo_letras += c
n = len(solo_letras)

print(solo_letras)

#verificar
texto_inv=solo_letras[::-1]

if solo_letras==texto_inv:
    print('Es palindromo')
else:
    print('No lo es')
