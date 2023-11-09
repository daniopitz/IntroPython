# Guía de Problemas Taller de Programación

---

### Problema 1: Frecuencia de elementos en una lista

#### Descripción:
Escribe una función llamada `frecuencia_elementos` que tome una lista y devuelva un diccionario donde las claves son los elementos únicos en la lista y los valores son la cantidad de veces que aparece cada elemento.


```python
[1, 2, 2, 3, 4, 3, 3] # entrada
{1: 1, 2: 2, 3: 3, 4: 1} #salida
```

### Problema 2: Conteo de vocales

#### Descripción:
Escribe una función llamada `contar_vocales` que reciba como argumento una cadena de texto y devuelva un diccionario con la cantidad de veces que cada vocal aparece en el texto.

```python
"hola mundo" #entrada
{'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1} #salida
```

### Problema 3: Conversión de dos listas a un diccionario

#### Descripción:
Escribe una función llamada `listas_a_diccionario` que tome dos listas `claves` y `valores` y devuelva un diccionario formado a partir de ellas.

```python
claves=['a', 'b', 'c'] #entrada
valores= [1, 2, 3] #entrada
{'a': 1, 'b': 2, 'c': 3} #salida
```

### Problema 4: Conversión de una lista de tuplas a un diccionario

Escribe una función llamada `tuplas_a_diccionario` que tome una lista de tuplas y devuelva un diccionario donde el primer elemento de cada tupla sea la clave y el segundo elemento sea el valor.

```python
[('1','Diamante'), ('4','Trebol'), ('K','Corazon')] #entrada
{'1': 'Diamante', '4': 'Trebol', 'K': 'Corazon'} #salida
```

### Problema 5: La tienda de comestibles

Estás encargado del inventario de una tienda de comestibles. Tienes un diccionario que representa el inventario actual de la tienda, donde las claves son los nombres de los productos y los valores son la cantidad disponible en la tienda. 

Recibes una lista de tuplas que representan un nuevo envío a la tienda. Cada tupla contiene el nombre del producto y la cantidad recibida. 

Escribe una función llamada `actualizar_inventario` que tome el diccionario de inventario actual y la lista de tuplas del nuevo envío, y devuelva un diccionario actualizado.

Ejemplo de uso:

```python
inventario_actual = {'manzana': 25, 'banana': 36, 'zanahoria': 50}
nuevo_envio = [('manzana', 10), ('zanahoria', 20), ('leche', 15)]
```

```python
inventario_actualizado = actualizar_inventario(inventario_actual, nuevo_envio)
print(inventario_actualizado)
```

```
{'manzana': 35, 'banana': 36, 'zanahoria': 70, 'leche': 15} #salida
```

### Problema 6: Calificación de exámenes

Eres un profesor y has dado un examen a tus alumnos. Cada examen se evalúa en una escala de 1 a 100. Escribe una función `resumen_calificaciones` que tome una lista de tuplas, donde cada tupla contiene el nombre del estudiante y su calificación, y devuelva un diccionario en el que las claves sean 'máxima', 'mínima', y 'media', y los valores sean tuplas que contengan el nombre del estudiante y la calificación correspondiente.

```python
[('Ana', 90), ('Bob', 85), ('Carla', 77)] #entrada
{'max': ('Ana', 90), 'min': ('Carla', 77), 'media': ('Promedio', 84)} #salida
```
