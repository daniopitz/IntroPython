# Guía de Ejercicios Taller de Programación UDD

### Ejercicio 1: Condicionales y Ciclos (Nivel Principiante)
**Descripción:** Escribe un programa que pida al usuario ingresar un número. Si el número es par, imprime "Es par". Si es impar, imprime "Es impar". Si es múltiplo de 5, imprime "Es múltiplo de 5".

**Conceptos Clave:** `if-else`, operadores de módulo (`%`).

### Ejercicio 2: Manejo de Listas (Nivel Intermedio)
**Descripción:** Crea un programa donde el usuario ingresa una serie de números (separados por comas). Convierte esta entrada en una lista y luego calcula la suma y el promedio.

**Conceptos Clave:** `input()`, `split()`, listas, `for`, `sum()`, `len()`.

### Ejercicio 3: Ciclo While (Nivel Principiante)
**Descripción:** Desarrolla un programa que pida al usuario ingresar palabras hasta que escriba "salir". Luego, muestra todas las palabras en orden inverso.

**Conceptos Clave:** `while`, `listas`, `append()`, inversión de lista.

###Ejercicio 4: Trabajo con Tuplas y Sets (Nivel Intermedio)
**Descripción:** Programa para ingresar tres números, almacenarlos en una tupla, convertirlos en un set y verificar duplicados.

**Conceptos Clave:** `tuplas`, `sets`, conversión de tipos.

### Ejercicio 5: Manejo de Strings: Método Split (Nivel Principiante)
**Descripción:** Pide al usuario ingresar una frase y usa `split` para dividirla en palabras. Imprime la cantidad de palabras.

**Conceptos Clave:** `input()`, `split()`, `len()`.

### Ejercicio 6: Uso de Replace y Join en Strings (Nivel Intermedio)
**Descripción:** Toma una frase del usuario, reemplaza espacios con guiones y luego usa `join` para unir las palabras con comas.

**Conceptos Clave:** `replace()`, `join()`.

### Ejercicio 7: Búsqueda y Manipulación de Strings (Nivel Avanzado)
**Descripción:** Busca una palabra clave en una frase larga ingresada por el usuario. Si se encuentra, reemplázala con la palabra al revés. Si no, indica que no está presente.

**Conceptos Clave:** `input()`, `index()`, slicing, condicionales.

### Ejercicio 8: Análisis de Frecuencia de Palabras en un Texto (Nivel Avanzado)
**Descripción:** Escribe un programa que pida al usuario ingresar un largo texto. El programa debe analizar el texto y calcular la frecuencia de aparición de cada palabra. Imprime las cinco palabras más frecuentes junto con su número de apariciones.

**Conceptos Clave:** manejo de `strings`, `listas`, `diccionarios`, `split()`, ciclos, ordenamiento de datos.

### Ejercicio 9: Cifrado César (Nivel Avanzado)
**Descripción:** Implementa el cifrado César en una función. Este cifrado desplaza cada letra del texto por un número fijo de posiciones en el alfabeto. El usuario debe ingresar un texto y el número de desplazamientos. Ejecute la función con una frase de prueba e imprima el texto cifrado. Asegúrese que el programa pueda manejar tanto mayúsculas como minúsculas y que ignore los caracteres que no sean letras. 

**Conceptos Clave:** manejo de `strings`, ciclos, condicionales, operaciones con caracteres.

**Ejemplo:**

1. **Texto Original:** "HOLA MUNDO"
2. **Desplazamiento:** 3
3. **Proceso de Cifrado:** Cada letra del texto se desplaza tres posiciones en el alfabeto. Por ejemplo, 'H' se convierte en 'K', 'O' en 'R', etc.
4. **Texto Cifrado:** "KROD PXQGR"

```python
texto_original = "HOLA MUNDO"
desplazamiento = 3
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto Original:", texto_original)
print("Texto Cifrado:", texto_cifrado)
```


### Ejercicio 10: Cálculo de Sumatoria y Producto Anidados (Nivel Avanzado)
**Descripción:** Implementa un programa que calcule la siguiente expresión matemática: 
$$\sum_{k=1}^{n} k \cdot \prod_{j=1}^{k} j$$

En esta expresión,  `n` es un número entero positivo ingresado por el usuario. Para cada entero `k` desde 1 hasta `n`, el programa debe calcular primero el producto de todos los enteros desde 1 hasta `k`, esto es ($\prod_{j=1}^{k} j$ ), luego multiplicar este producto por `k`y finalmente sumar todos estos resultados.

**Ejemplo:**
Si el usuario ingresa `n = 3`, el programa debe realizar los siguientes cálculos:

1. Para `k = 1`: El producto de números desde 1 hasta 1 es 1, luego $1 \cdot 1 = 1$.

2. Para `k = 2`: El producto de números desde 1 hasta 2 es $1 \cdot 2 = 2 $, luego $ 2 \cdot 2 = 4 $.

3. Para `k = 3`: El producto de números desde 1 hasta 3 es $ 1 \cdot 2 \cdot 3 = 6 $, luego $3 \cdot 6 = 18 $.
 
La sumatoria de estos resultados es `1 + 4 + 18 = 23`. Por lo tanto, el programa debe imprimir 23.

**Conceptos Clave:** ciclos anidados, operaciones matemáticas, manejo de entrada del usuario.





