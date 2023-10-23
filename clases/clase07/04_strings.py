s = "Hola mundo!"
print('tamano s', len(s))

# concatenar
s1 = 'Hola' + ' '
s2 = 'Chao'
s3 = s1 + s2
print('s1 + s2:', s3)

# acceso, la primera posicion comienza en 0
print('Primer elemento s:', s1[1]) 

# substring
s4 = s[1:7]
print('s[2:5] = ', s4)

# actualizar string: reemplazar ?
#s='Hola mundo'
#s[0]='T'
#print(s)

# actualizar string: concatenar
#print(s[1:])
#s = "T" + s[1:]
#print(s)

# actualizar string: reemplazar
s=s.replace('H','T')
print(s)






