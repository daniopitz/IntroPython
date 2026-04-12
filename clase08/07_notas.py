n = int(input('Ingrese número de estudiantes: '))

i = 0

while i < n:
    suma = 0

    nota1 = float(input('Ingrese nota 1: '))
    nota2 = float(input('Ingrese nota 2: '))
    nota3 = float(input('Ingrese nota 3: '))

    suma = nota1 + nota2 + nota3
    promedio = suma / 3

    print('Promedio estudiante', i + 1, ':', round(promedio, 1))
    print()

    i += 1
