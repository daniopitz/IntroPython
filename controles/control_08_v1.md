### PrograUDD. Control 8 Versión 1

**Instrucciones**: Resuelva el siguiente ejercicio. Suba su solución como un archivo `c08_apellido_nombre.py` a Canvas, Sección Tareas > Ayudantías. 

**Reprobados**. 

1. Haga un programa que lea un archivo con la siguiente información: los nombres de los estudiantes del Taller de Programación y sus notas finales del curso, y calcule cuántos de ellos han reprobado el ramo. Un estudiante reprueba el ramo si tiene una nota final inferior a 4.0.
2. Use el archivo `notas_taller_progra.txt` que se encuentra disponible en la sección **Archivos**<**Ayudantías**.

Solucion: 6 puntos totales

```python
#Abrir correctamente el archivo 0.3 pts
with open('notas_taller_progra.txt', 'r') as f:    
    reprobados=0 #inicializar un contador 0.5 pts
    
    for line in f: #iterar sobre el archivo 0.5 pts
    
        #Separar en una lista usando el separador correcto 1.0 pt
        aux=line.split(';')        
        #Seleccionar la columna correcta y transformar a float  1.0 pt
        nota=float(aux[1])        
        if nota < 4.0: #Filtrar los reprobados 1.0 pt
            reprobados+=1 #Contar correctamente 1.0 pt

#Imprimir el valor correcto 0.7 pts 
print('El numero de reprobados es:', reprobados) 

```
