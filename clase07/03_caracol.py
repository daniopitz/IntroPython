distancia = 50

while distancia > 0:
    avance = int(input('¿Cuántos cm avanzó el caracol? (1-10): '))

    if avance < 1 or avance > 10:
        print('Debe ser entre 1 y 10 cm.')
    elif avance > distancia:
        print(f'Solo le faltan {distancia} cm.')
    else:
        distancia = distancia - avance
        print(f'Le faltan {distancia} cm')

print('¡El caracol llegó a la meta!')
