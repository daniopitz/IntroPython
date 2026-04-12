# Strings en Python

# Se pueden usar diferentes tipos de comillas:
print('Hola')
print("Hola")
print('''Hola''')


# Strings son secuencias ordenadas y se pueden indexar
s = 'Hola'
print("s[0] →", s[0])      # primer carácter → 'H'
print("s[-1] →", s[-1])    # último carácter → 'a'

# Slicing (cortes)
print("s[0:2] →", s[0:2])  # subcadena del índice 0 al 1 → 'Ho'
print("s[2::] →", s[2::]) # subcadena del índice 2 hasta el final → 'la'

# Concatenación
print("Concatenar: " + "Hola" + " Mundo")

# Repetición
print("Repetir: " + ("Hi" * 3))  # "HiHiHi"

# Pertenencia
texto = "universidad tecnica"
print("'tec' in texto →", "tec" in texto)
print("'usm' in texto →", "usm" in texto)
print("'U' in texto →", "U" in texto)
