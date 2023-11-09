# Taller de Programación - Certamen (Tarea 2)

Fecha: 8 de Noviembre del 2023

## Instrucciones Generales

- Resuelva en parejas el siguiente problema utilizando todo lo aprendido en clases.
- Su código debe estar contenido en un único archivo `t2_nombre_apellido.py`.

## Detalles de la Entrega

- La fecha de entrega es el **20 de Noviembre del 2023**.
- Debe enviar su archivo `.py` a través de Canvas

## Contexto

En el contexto de una aplicación para la gestión de una biblioteca, se requiere implementar un sistema para manejar la información de libros, usuarios y préstamos. La información debe ser almacenada utilizando estructuras de datos adecuadas y se debe permitir la interacción con el usuario a través de la consola para realizar consultas y actualizaciones.

## Reglas
1. Los libros están contenidos en un archivo  llamado  `catologo_libros.txt` de cuatro columnas: `id`, `titulo`, `autor` y `año_publicacion`.
2. Los libros deben representarse por tuplas con la siguiente información: `(id, titulo, autor, año_de_publicacion)`. 
3. Los prestamos deben representarse por un diccionario que contenga los IDs de los usuarios (llave) y los libros que tienen en préstamo (valores). Por ejemplo, en `prestamos= {'1': ['6','78','22'], '2': ['40', '50']}` el usuario  de ID `'1'` tiene tres libros en prestamo: `['6','78','22']` y así susesivamente.
 
4. Se debe mantener un archivo `prestamos.txt` que contenga el ID del usuario y los IDs de los libros prestados, uno por línea, separados por comas.
5. El programa debe ser capaz de:
    - Añadir y remover libros del catálogo.
    - Registrar préstamos y devoluciones actualizando tanto la estructura en memoria como el archivo de préstamos.
    - Buscar libros por autor o año de publicación.
    - Mostrar todos los préstamos de un usuario.

## Funciones

Define las siguientes ocho funciones a implementar. Estas funciones abarcarán las operaciones principales del sistema de la biblioteca.

1. `cargar_catalogo(archivo)` [10 puntos]: Carga el catálogo de libros desde un archivo y lo retorna como una **lista de tuplas**.

2. `agregar_libro(catalogo, libro)` [10 puntos]: Agrega un libro al catálogo. La variable `libro` es una **tupla** con la información del libro.

3. `eliminar_libro(catalogo, libro_id)` [10 puntos]: Elimina un libro del catálogo basado en su ID.

4. `cargar_prestamos(archivo)` [10 puntos]: Carga los préstamos desde un archivo y los retorna como un **diccionario** donde la clave es el ID del usuario y el valor es una lista con los IDs de los libros prestados.

5. `registrar_prestamo(prestamos, usuario_id, libro_id)` [15 puntos]: Registra un préstamo en la estructura de préstamos y actualiza el archivo de préstamos.

6. `registrar_devolucion(prestamos, usuario_id, libro_id)` [15 puntos]: Registra una devolución en la estructura de préstamos y actualiza el archivo de préstamos.

7. `buscar_libros(catalogo, criterio, valor)` [15 puntos]: Busca libros en el catálogo basándose en un criterio específico (por ejemplo, autor o año) y retorna una **lista de libros** que cumplen con ese criterio.

8. `listar_prestamos_usuario(prestamos, usuario_id)` [15 puntos]: Lista todos los préstamos de un usuario específico. Debe entregar una **lista.**

Cada función deberá ser diseñada para manejar posibles errores, como entradas inválidas o situaciones en las que un libro no pueda ser eliminado porque está prestado.

## Ejemplo

Un ejemplo de cómo podrían lucir las primeras lineas del archivo `catalogo.txt` después de algunas operaciones sería:

```python
id, nombre_del_libro, autor, año_de_publicación
1, "La casa de los espíritus", Isabel Allende, 1982
2, "1984", George Orwell, 1949
3, "Los detectives salvajes", Roberto Bolaño, 1998
4, "Cien años de soledad", Gabriel García Márquez, 1967
5, "Los altísimos", Hugo Correa, 1959
7, "Orgullo y prejuicio", Jane Austen, 1813
8, "Moby Dick", Herman Melville, 1851
9, "Subterra", Baldomero Lillo, 1904
10, "El gran Gatsby", F. Scott Fitzgerald, 1925
11, "El túnel", Ernesto Sabato, 1948
```

Y como podría lucir el archivo `prestamos.txt` después de algunas operaciones:

```python
1, 6, 78, 22
2, 40, 51
3, 95, 12, 73
```

Aquí, el usuario con ID 1 tiene los libros con IDs 6, 78 y 22, y así sucesivamente.
