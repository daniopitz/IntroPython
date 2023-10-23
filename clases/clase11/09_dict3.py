d = {"Python": 1991, "C": 1972, "Java": 1996}
#Imprimiendo llaves
print('Llaves')
print('------------------------------------')
for lenguaje in d.keys():
    print(lenguaje)
print('------------------------------------')

print('Valores')
print('------------------------------------')
#Imprimiendo valores
for fecha in d.values():
    print(fecha)
print('------------------------------------')   

print('Llaves y valores')
print('------------------------------------')
#Imprimiendo llave y valor al mismo tiempo
for lenguaje,año in d.items():
    print(lenguaje, año)
print('------------------------------------')