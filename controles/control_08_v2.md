### PrograUDD. Control 8 Version 2

**Instrucciones**: Resuelva el siguiente ejercicio. Suba su solución como un archivo `ay07_apellido_nombre.py` a Canvas, Sección Tareas > Ayudantías. 

**Prendas pequeñas.** 

1. Haga un programa que lea un archivo con la siguiente información: prendas de vestir (productos de una tienda) y sus respectivas tallas disponibles, y calcule cuántas prendas hay de tallas pequeñas. Las tallas pequeñas son **xs** y **s**. Su programa debe retornar el número de prendras en total (la suma de `xs` y `s`).

2. Use el archivo `tallas_prendas.txt` que se encuentra disponible en la sección **Archivos**<**Ayudantías**.

Solucion: 6 puntos

``` python
#Abrir el archivo correctamnte en modo lectura 0.3 pts
with open ('tallas_prendas.txt', 'r') as f:
    contador=0 #Inicializar el contador 0.5 pts
    
    for line in f: #Iterar sobre el archivo 0.5 pts
        aux=line.split(',') #Separar en una lista 1.0 pt
        producto=aux[0] #Seleccionar la columna de tallas 0.5 pts
        talla=aux[1].strip('\n') #Quitar salto de linea 0.5 pts

        if talla=='s' or talla=='xs': #Filtar 1.0 pt
            print(producto, talla)
            contador+=1 #Contar las tallas correctas 1.0 pt
            
#Imprimir el resultado correctamente (valor correcto) 0.7 pts
print('El numero de tallas pequeñas es', contador) 
```