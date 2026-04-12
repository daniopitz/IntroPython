asientos = 20
vendidos = 0

print('Asientos disponibles:',asientos)

while asientos > 0:
    boletos = int(input('¿Cuántos boletos desea? '))

    if boletos < 1 or boletos > 4:
        print('Debe comprar entre 1 y 4 boletos.')
    elif boletos > asientos:
        print('No hay suficientes asientos. Solo quedan ', asientos )
    else:
        asientos = asientos - boletos
        vendidos = vendidos + boletos
        print(f'Asientos restantes: {asientos}')

print('Función terminada. Se vendieron', vendidos, 'boletos.')
