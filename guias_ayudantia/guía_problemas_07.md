# Guía de Problemas Taller de Programación

---

### Problema 1: Principiante
**Objetivo:** Leer un archivo que contiene una lista de nombres (uno por línea) y guardarlos en una **lista** en Python.

- **Funciones a utilizar:** `leer_nombres(archivo)`
- **Archivo de entrada (nombres.txt):**

```python
Ana
Juan
Maria
```

### Problema 2: Principiante-Intermedio
**Objetivo:** Leer un archivo que contiene pares de datos (nombre, edad) separados por comas en cada línea y almacenarlos en una **lista de tuplas**.

- **Funciones a utilizar:** `leer_datos_personales(archivo)`
- **Archivo de entrada (datos_personales.txt):**

```python
Ana, 30
Juan, 25
Maria, 28
```

### Problema 3: Intermedio
**Objetivo:** Leer un archivo con datos de productos en formato "ID, Nombre, Precio" y almacenarlos en un **diccionario donde el ID es la clave y el valor es otra tupla con nombre y precio**.

- **Funciones a utilizar:** `leer_productos(archivo)`
- **Archivo de entrada (productos.txt):**

```python
001, Manzana, 0.50
002, Pan, 1.00
003, Leche, 0.80
```

### Problema 4: Intermedio-Avanzado

**Objetivo:** Leer un archivo con datos de alumnos (ID, nombre, calificaciones) y almacenarlos en un diccionario donde la clave es el ID y el valor es otro diccionario con el nombre del alumno y su lista de calificaciones.

- **Funciones a utilizar:** `leer_calificaciones(archivo)`
- **Archivo de entrada (calificaciones.txt):**

```python
001, Ana, 90, 85, 88
002, Juan, 75, 80, 78
003, Maria, 92, 88, 91
```

### Problema 5: Avanzado

**Objetivo:** Leer un archivo de texto que contiene un párrafo y contar la frecuencia de cada palabra, almacenando los resultados en un diccionario.

- **Funciones a utilizar:** `contar_palabras(archivo)`
- **Archivo de entrada (texto.txt):**

``` python
La inteligencia artificial es una fascinante área de la ingeniería y la ciencia. Tiene el potencial de
revolucionar muchos aspectos de nuestra vida cotidiana, desde la forma en que interactuamos con la
tecnología hasta cómo resolvemos problemas complejos. Como estudiantes de ingeniería en su primer año, 
están al borde de explorar y contribuir a este campo emocionante. Ustedes tienen la oportunidad de ser 
parte de esta revolución tecnológica, de aprender y de crear soluciones que aún no podemos imaginar. 
El camino para entender y aprender a utilizar las herramientas de inteligencia artificial comienza con 
pequeños pasos como este ejercicio. ¡Estén listos para ser parte de algo grande!
```

### Problema 6: Avanzado

**Objetivo:** Leer un archivo con datos de ventas (fecha, producto, cantidad) y escribir un nuevo archivo con un resumen de ventas por producto.

- **Funciones a utilizar:** `resumen_ventas(archivo_entrada, archivo_salida)`
- **Archivo de entrada (ventas.txt):**


```python
2023-01-01, Manzana, 50
2023-01-01, Pan, 30
2023-01-02, Leche, 20
2023-01-03, Pan, 10
```

- **Archivo de salida (ventas_total.txt):**

```python
Manzana, 50
Pan, 40
Leche, 20
```

### Problema 7: Muy Avanzado
 
**Objetivo:** Leer un archivo con información de empleados (ID, nombre, departamento) y generar un nuevo archivo que agrupe a los empleados por departamento.

- **Funciones a utilizar:** `agrupar_empleados(archivo_entrada, archivo_salida)`


- **Archivo de entrada (empleados.txt):**

```python
001, Ana, Ventas
002, Juan, Marketing
003, Maria, Ventas
004, Miguel, RR.HH
```

- **Archivo de salida (departamentos.txt):**

```python
Ventas: Ana, Maria
Marketing: Juan
RR.HH: Miguel
```

### Problema 8: Muy Avanzado

Desarrollar funciones para leer datos de un archivo de medallas de los juegos Panamericanos y calcular estadísticas básicas.
 
**Objetivo 1:** Escriba una funcion que reciba el nombre de un archivo con las medallas por país de los juegos panamericanos y retorne una lista de tuplas, donde cada tupla contiene el país (str) y el tipo de medalla (str).

- **Funciones a utilizar:** `leer_medallas(medallas)`

- **Archivo de entrada (medallas.txt):**

```python
País          Oro    Plata    Bronce    Total
Brasil           50    40       60        150
Canadá           60    50       40        150
México           30    45       55        130
Argentina        20    30       50        100
Colombia         15    25       35         75
Perú             10    15       20         45
Chile            35    10       15         60
```
- **Salida:**

```python
[ ("Brasil", 50, 40, 60), ("Canadá", 60, 50, 40), ("México", 30, 45, 55),...]
```

**Objetivo 2:** Crear un ranking de países basado en un sistema de puntos (3 puntos por oro, 2 por plata, 1 por bronce). Crear un archivo nuevo ordenado segun el número de puntos por país de mayor a menor.

- **Funciones a utilizar:** `generar_ranking(lista_tuplas)`

- **Archivo de salida (ranking.txt):**

```python
Canadá: 320 puntos
Brasil: 290 puntos
México: 235 puntos
Argentina: 170 puntos
Chile: 140 puntos
Colombia: 130 puntos
Perú: 80 puntos
```