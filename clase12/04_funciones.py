def contar_vocales(frase):
    suma=0
    for letra in frase:
        if letra in 'aeiou':
            suma=suma+1
            
    return suma


def tienes_muchas_vocales(frase2):
    print(contar_vocales(frase2))
    if contar_vocales(frase2)>10:
        return True
    else:
        return False
    
print(tienes_muchas_vocales('Hola'))
    
    
