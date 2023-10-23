from random import random
#Inicializando matriz de ceros

def fillrandom(matrix2, rows2, cols2):
    for fila in range(rows2):#iterar sobre las filas
        for columna in range(cols2):#iterar sobre las columnas
            matrix2[fila][columna] = random()


rows = 2
cols = 3
matrix = []

for i in range(rows):
    matrix.append([0]*cols)
    
print("Matriz de ceros")
print(matrix)
print('\n')

print("Matriz random")
fillrandom(matrix, 2, 2)

print(matrix)



            
            
            