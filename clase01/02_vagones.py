n_fila=int(input('Ingresa el número de personas en la fila'))
n_vagon= int(input('Ingresa la capacidad del vagón'))

#solucion
print('Vagones completos:', n_fila//n_vagon)
print('Personas que quedan en la fila:', n_fila%n_vagon)
