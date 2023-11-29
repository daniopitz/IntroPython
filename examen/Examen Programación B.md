<div align="center">
<img src="logo_UDD_Facultad_Ingenieria.png" style="float: center; height: 80px;" >
</div>


<h3 align="center">Taller de Programación</h3>
<h4 align="center">Examen</h4>
<h5 align="center">28 de noviembre de 2023</h5>

**Nombre**:..................................................................................................................


### Instrucciones:

- Lea atentamente el enunciado de cada uno de los problemas.
- Los problemas 1 y 2 son **obligatorios**. Debe escoger entre el problema 3 y 4.
- Para cada problema cree un archivo.py distinto. El nombre del archivo debe ser el número del problema (uno.py, dos.py, tres.py, cuatro.py).
- Comprima los problemas en un solo archivo ZIP y súbalo a la sección Evaluación en http://canvas.udd.cl. Solo tiene una oportunidad para subir sus respuestas.
- No se puede utilizar librerías adicionales ni estilos de sintaxis o métodos avanzados de programación que no se hayan revisado en clases o que no domine.
- En caso de que su profesor(a) tenga dudas sobre la originalidad del código, podrá interrogarlo oralmente para verificar que no hubo faltas a la ética.
- De detectarse copia entre pares o cualquier otra situación que de cuenta de falta a la ética, su certamen será evaluado con la NOTA MÍNIMA y será reportado(a) al comité de ética de la Facultad, lo que puede derivar en una causal de eliminación de la universidad.

### Ejercicio 1 Obligatorio: Registro de Ventas de una Librería (2.5 pts)


Desarrolla un programa que gestione el registro de ventas de una librería y genere un resumen específico. El archivo de registro de ventas contiene una fila por libro y tiene la siguiente estructura:

**Columnas:** Fecha, Título del libro, Autor, Precio.


Cree un programa que lea el archivo CSV `ventas_libreria.csv` y escriba un archivo llamado `resumen_ventas_Coelho.csv`.

Este archivo debe contener el autor, título del libro, y cantidad total vendida **sólo para el autor "Coelho"**.

**Ejemplo de archivo de salida:**

```python
Autor;Titulo;CantidadTotal
Coelho;Brida;4
Coelho;El Alquimista;12
```

---

### Ejercicio 2 Obligatorio: Diccionarios y Funciones (2.5 pts)



Crea una **función** `contar_palabras_inician_vocal` que tome una frase como entrada y devuelva un diccionario donde las claves sean las palabras presentes en la frase que empiezan con una vocal y los valores sean la cantidad de veces que cada palabra aparece.

**Nota**: 
- La función `letra.lower()` en el caso de que una letra sea mayuscula la transforma a una letra minuscula.

### Ejercicio 3: Manejo de Tuplas (1.0 pt)



Escribe un programa que solicite al usuario ingresar N coordenadas en formato `x, y`. Luego, almacena estas coordenadas en una lista de tuplas y luego muestra por pantalla los valores obtenidos.

**Ejemplo de entrada:**
```
2,3
```


---

### Ejercicio 4: Condicionales y Ciclos (1.0 pt)

#### Descripción

Desarrolla una **función** `suma_raiz_cuadrada_pares` que reciba un número `n` y calcule la suma de las raíces cuadradas de todos los números pares desde 1 hasta 'n'. Recuerde que un número par puede ser representado por la expresión $2\dot k$. Y que el método `sqrt(numero)` de la librería `math` permite calcular la raíz cuadrada de un número.


---

