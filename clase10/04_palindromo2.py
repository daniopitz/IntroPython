texto = input('Ingrese texto:')
texto = texto.lower()

#quitar espacio
n = len(texto)
solo_letras = ''
for c in texto:
    if c != ' ':
        solo_letras += c
n = len(solo_letras)


#verificar palindromo
verificador = True
i = 0
while i < n//2:
    if solo_letras[i] != solo_letras[n-1-i]:
        verificador = False
    i += 1
if verificador:
    print('Es palindromo')
else:
    print('No lo es')
