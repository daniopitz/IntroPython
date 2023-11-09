### Control 07 Version 1

**Instrucciones**: Resuelva el siguiente ejercicio. Suba su solución como un archivo `c07_apellido_nombre.py` a Canvas, Sección Tareas > Ayudantías. 

**Notas del Curso**. 

1- Escriba un programa o función que reciba como argumento una **lista de tuplas** con el nombre de los estudiantes del curso  y las tres primeras 3 notas de sus ayudantías. Luego, a partir de dicha información construya un diccionario en el que  guarde los nombres como llaves (claves o keys), y el promedio de sus 3 notas de ayudantías como valor. 

Ejemplo:

Si tenemos la siguiente información para tres estudiantes:

```python
lista=[('Manuel', [5.9, 6.3, 7.0]), ('Ana', [7.0, 6.8, 7.0]), ('Pedro', [2.1, 4.0, 3.3])]
```

```python
notas_dicc= {'Manuel': 6.4, 'Ana': 6.9, 'Pedro': 3.1}
```

Solución 1:


```python
def notas_curso(entrada):
    promedio = dict()
    
    for estudiante in entrada:
        nombre = estudiante[0] #elemento 0, nombre
        notas = estudiante[1] #elemento 1, lista de notas
        prom = sum(notas)/len(notas)
        prom = round(prom, 1)       ## redondeo, no es necesario
        promedio[nombre] = prom
	return promedio
```



2- Escriba una función que reciba el diccionario anterior y retorne una **tupla** que contenga la mejor y peor nota promedio del curso. El código debe funcionar para un número cualquiera de estudiantes.

El resultado final deberia verse así: 

```python
(6.4, 3.1)
```

Solución 2:

```python
def nota_min_max(entrada):
    notas = []
    for prom in entrada.values(): #accedo a los valores
        notas.append(prom)
    minima = min(notas)
    maxima = max(notas)
    min_max = (maxima, minima) #le doy el formato de una tupla
    return min_max
```