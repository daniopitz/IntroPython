texto=input('Ingrese texto: ')
contador=0
i=1
while i <len(texto):
    if (texto[i]=='a') or (texto[i]=='e') or (texto[i]=='i') or (texto[i]=='o') or (texto[i]=='u'):
        print(texto[i])
        contador+=1
    i=i+1
        

print(contador)    
