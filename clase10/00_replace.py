texto=input('Ingrese una palabra en minuscula: ')
texto=texto[0].upper() + texto[1:len(texto)-1] + texto[-1].upper()
print(texto)

