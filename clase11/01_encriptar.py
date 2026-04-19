clave='murcielago'
palabra='mundo'

palabra_nueva=''
for letra in palabra:
    if letra in clave:
        i=0
        while i < len(clave):
            if letra==clave[i]:
                indice=i
            i=i+1
        palabra_nueva+=str(indice)
    else:
        palabra_nueva+=letra

print(palabra_nueva)


        


