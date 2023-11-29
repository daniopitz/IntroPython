# Información para poner en la pizarra:
#   función round(a, b) retorna el número a redondeado con b decimales
#       a = 6.3999999999999995
#       b = 1
#       redondeado = round(a, b) -> redondeado = 6.4
#

def notas_curso(estudiantes, notas_ayudantias):
    promedio = {}
    
    for i in range(len(estudiantes)):        
        nombre = estudiantes[i]
        notas = notas_ayudantias[i]
        prom = sum(notas)/len(notas)
        prom = round(prom, 1)       ## necesario
        promedio[nombre] = prom
            
    return promedio
    
def nota_min_max(entrada):
    notas = []
    for prom in entrada.values():
        notas.append(prom)
    minima = min(notas)
    maxima = max(notas)
    min_max = (maxima, minima)
    return min_max
    
    
lista_nombres = ['Manuel', 'Ana', 'Pedro']
lista_notas = [[5.9, 6.3, 7.0],[7.0, 6.8, 7.0],[2.1, 4.0, 3.3]]

notas = notas_curso(lista_nombres, lista_notas)
print(notas)


minmax = nota_min_max(notas)
print(minmax)


## Con las siguientes líneas evalué que el resultado de la función
## notas_curso calcula correctamente los promedios.


# Pregunta 1
esperado_preg_1 = {'Manuel': 6.4, 'Ana': 6.9, 'Pedro': 3.1}
# salida_esperada = {'Manuel': 6.3999999999999995, 'Ana': 6.933333333333334, 'Pedro': 3.133333333333333}

if notas == esperado_preg_1:
    print("OK Pregunta 1")
else:
    print("Failed Pregunta 1")

# Pregunta 1
esperado_preg_2 = (6.9, 3.1)

if minmax == esperado_preg_2:
    print("OK Pregunta 2")
else:
    print("Failed Pregunta 2")

