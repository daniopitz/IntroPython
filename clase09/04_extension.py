texto=input('Ingrese nombre del archivo:')

i=0
while i < len(texto):
    if texto[i]=='.':
        nombre=texto[0:i]
        extension=texto[i+1:len(texto)]
    i=i+1
  

print('Nombre:',nombre)
print('Extension:',extension)

        
