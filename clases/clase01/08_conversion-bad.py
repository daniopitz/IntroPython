num_amigos = input('Cuantos amigues tienes en facebook? ')
num_amigos2 = int(num_amigos)
num_comun = int(input('Cuantos amigues tienes en comun con tu mejor amigue? '))


porcentaje = num_comun/num_amigos2*100

print('Wow, tienes', porcentaje, '% de amigues en comun con tu mejor amigue!')

print('tipo variable amigos:', type(num_amigos))
print('tipo variable num_amigos:', type(num_amigos2))