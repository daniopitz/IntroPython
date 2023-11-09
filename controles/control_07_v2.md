### Control 07 Version 2

**Instrucciones**: Resuelva el siguiente ejercicio. Suba su solución como un archivo `c07_apellido_nombre.py` a Canvas, Sección Tareas > Ayudantías. 

**Notas del Curso**. 

1- Escriba un programa o función que reciba como argumento **dos listas**, una con el nombre de los estudiantes del curso  y otra con **una lista** con las tres primeras 3 notas de sus ayudantías (lista de listas). Luego, a partir de dicha información construya un diccionario en el que  guarde los nombres como llaves (claves o keys), y el promedio de sus 3 notas de ayudantías como valor. 

Ejemplo:

Si tenemos la siguiente información para tres estudiantes:

```
lista_nombres=['Manuel', 'Ana', 'Pedro']
lista_notas=[[5.9, 6.3, 7.0],[7.0, 6.8, 7.0],[2.1, 4.0, 3.3]]
```

```
notas_dicc= {'Manuel': 6.4, 'Ana': 6.9, 'Pedro': 3.1}
```

2- Escriba una función que reciba el diccionario anterior y retorne una **tupla** que contenga la mejor y peor nota promedio del curso. El código debe funcionar para un número cualquiera de estudiantes.



El resultado final deberia verse así: 

```
(6.4, 3.1)