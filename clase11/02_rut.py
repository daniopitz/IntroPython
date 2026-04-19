rut_base='16126791'
verificador='1'
digitos='32765432'
suma=0

i=0
while i <len(rut_base):
    suma+=int(rut_base[i])*int((digitos[i]))
    i=i+1

resto=suma%11
d=11-resto

if d==10 and (verificador=='k') or (verificador=='K'):
    print('Es correcto')
elif d==11 and (verificador=='0'):
    print('Es correcto')

elif d==int(verificador):
    print('Es correcto')

else:
    print('Es falso')

   
    
    
