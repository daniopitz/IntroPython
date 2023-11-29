#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cargar_catalogo(archivo):
    with open(archivo, "r") as f:
        next(f)
        catalogo = []
        for line in f:
            aux = line.split(",")
            catalogo.append((aux[0], aux[1], aux[2], int(aux[3])))
    return catalogo


def guardar_catalogo(archivo, catalogo):
    header = ",".join(["id", "nombre_del_libro", "autor", "año_de_publicación"]) + "\n"

    with open(archivo, "w") as h:
        h.write(header)
        for libro in catalogo:
            libro = list(libro)
            libro[-1] = str(libro[-1])
            linea = ",".join(libro) + "\n"
            h.write(linea)


def agregar_libro(catalogo, libro):
    print("Agregando", libro, "a catalogo general")
    catalogo.append(libro)

    print("Catalogo general actualizado")
    return catalogo


def eliminar_libro(catalogo, libro_id):
    ids = list()
    for libro in catalogo:
        ids.append(libro[0])
    if libro_id not in ids:
        print("El libro no pudo ser eliminado porque no está en el catalogo")

    else:
        print("Eliminando libro", libro_id, "del catalogo")

        for libro in catalogo:
            if libro[0] == libro_id:
                catalogo.remove(libro)

    return catalogo


def cargar_prestamos(archivo):
    dicc_prestamos = dict()
    with open(archivo, "r") as g:
        for line in g:
            libros = line.split(",")
            ID = libros[0]
            n = len(libros)
            libros[-1] = libros[-1].strip("\n")
            dicc_prestamos[ID] = libros[1:n]
    return dicc_prestamos


def buscar_libros(catalogo_lista, criterio, valor):
    libros = list()
    a = 0
    if criterio in ["id", "nombre", "año", "autor"]:
        for libro in catalogo_lista:
            if criterio == "id" and libro[0] == valor:
                libros.append(libro)
                a += 1
                break

            elif criterio == "nombre" and libro[1] == valor:
                libros.append(libro)
                a += 1
                break

            elif criterio == "autor" and libro[2] == valor:
                libros.append(libro)
                a += 1
                break

            elif criterio == "año" and libro[3] == valor:
                libros.append(libro)
                a += 1
                break
        print("Libros encontrados:", libros)

    else:
        print("Criterio de busqueda incorrecto")

    if a == 0:
        print("No se encontraron registros para", criterio, "igual a", valor, end=" ")

    return libros


def listar_prestamos_usuario(prestamos, usuario_id):
    print("Buscando prestamos del usuario", usuario_id)
    if usuario_id in prestamos:
        return prestamos[usuario_id]
    else:
        print("El usuario", usuario_id, "no registra prestamos", end=" ")
        return []


def guardar_prestamos(archivo, prestamos):
    with open(archivo, "w") as h:
        for llave, libros in prestamos.items():
            linea = ",".join([llave] + libros) + "\n"
            h.write(linea)


def registrar_prestamo(catalogo, prestamos, usuario_id, libro_id):
    print("Buscando libro", libro_id, "en catalogo")
    # catalogo_lista = cargar_catalogo(catalogo)

    ids_libros = list()

    for libro in catalogo:
        ids_libros.append(libro[0])

    if libro_id not in ids_libros:
        print("Este libro no está en el catalogo")
    else:
        print("Libro", libro_id, "es parte del catalogo")
        print("Prestando libro", libro_id, "a usuario", usuario_id)

        if usuario_id in prestamos:
            print("Usuario", usuario_id, "tiene libros en prestamo")
            prestamos[usuario_id].append(libro_id)
            print("Se ha prestado libro", libro_id, "a  usuario", usuario_id)

        else:
            print("Usuario", usuario_id, "no tiene libros en prestamo")
            prestamos[usuario_id] = [libro_id]
            print("Se ha prestado libro", libro_id, "a usuario", usuario_id)
        catalogo = eliminar_libro(catalogo, libro_id)
    return catalogo, prestamos


def registrar_devolucion(catalogo, original, prestamos, usuario_id, libro_id):
    print(
        "Buscando libro", libro_id, "prestado a", usuario_id, "en catalogo de prestamos"
    )

    if usuario_id not in prestamos:
        print("Usuario no encontrado")

    else:
        print("Tu usuario está registrado:")
        for usuarios, libros in prestamos.items():
            if usuarios == usuario_id:
                if libro_id in libros:
                    print("El libro", libro_id, "ha sido encontrado")
                    libros.remove(libro_id)
                else:
                    print(
                        "No hay registro de prestamo del libro",
                        libro_id,
                        "al usuario",
                        usuario_id,
                    )

        libro_devuelto = buscar_libros(original, "id", libro_id)
        catalogo.append(libro_devuelto[0])

    return catalogo, prestamos


def print_catalogo(catalogo):
    print()
    print("--- Inicio catalogo")
    for libro in catalogo:
        print("---", libro)
    print("--- Fin catalogo")
    print()


def print_prestamos(prestamos):
    print()
    print("--- Inicio prestamos")
    for nombre, libros in prestamos.items():
        print("---", nombre, libros)
    print("--- Fin prestamos")
    print()


def demo():
    # Cargar Catalogo
    print("Pregunta 1: Cargando Catalogo:")
    catalogo_libros = cargar_catalogo("catalogo.txt")
    catalogo_libros_original = catalogo_libros.copy()

    print_catalogo(catalogo_libros)

    print("\n")

    # Agregar Libro
    print("Pregunta 2: Agregar Libro" + "\n")
    libro_nuevo = ("12", "El Principito", "Antoine de Saint-Exupéry", 1943)

    catalogo_libros = agregar_libro(catalogo_libros, libro_nuevo)
    catalogo_libros_original = catalogo_libros.copy()

    print_catalogo(catalogo_libros)

    print("\n")

    print("Pregunta 3: Eliminar Libro (ENCONTRADO)" + "\n")
    catalogo_libros = eliminar_libro(catalogo_libros, "9")
    catalogo_libros_original = catalogo_libros.copy()
    print_catalogo(catalogo_libros)

    print("\n")

    print("Pregunta 3: Eliminar Libro (NO encontrado)" + "\n")
    catalogo_libros = eliminar_libro(catalogo_libros, "42")
    catalogo_libros_original = catalogo_libros.copy()
    print_catalogo(catalogo_libros)

    print("\n")

    print("Pregunta 4: Cargar Prestamos" + "\n")
    prestamos_libros = cargar_prestamos("prestamos.txt")
    print_prestamos(prestamos_libros)
    print("\n")

    print("Pregunta 7: Buscar Libro (año 1948)" + "\n")
    print_catalogo(catalogo_libros)
    buscar_libros(catalogo_libros, "año", 1948)
    print("\n")

    print("Pregunta 7: Buscar Libro (criterio no existe)" + "\n")
    buscar_libros(catalogo_libros, "pais", "Chile")
    print("\n")

    print("Pregunta 7: Buscar Libro (criterio correcto, no existe)" + "\n")
    print_catalogo(catalogo_libros)
    buscar_libros(catalogo_libros, "año", 1951)
    print("\n")

    print("Pregunta 8: Buscar Usuario (con prestamos)" + "\n")
    print_prestamos(prestamos_libros)
    print(listar_prestamos_usuario(prestamos_libros, "1"))

    print("Pregunta 8: Buscar Usuario (no existe usuario)" + "\n")
    print_prestamos(prestamos_libros)
    print(listar_prestamos_usuario(prestamos_libros, "24"))
    print("\n")

    print("Pregunta 5: Registrar Prestamo" + "\n")
    print_catalogo(catalogo_libros)
    print_prestamos(prestamos_libros)
    catalogo_libros, prestamos_libros = registrar_prestamo(
        catalogo_libros, prestamos_libros, "3", "11"
    )
    print_catalogo(catalogo_libros)
    print_prestamos(prestamos_libros)
    print("\n")

    print("Pregunta 5: Registrar Prestamo" + "\n")
    print_prestamos(prestamos_libros)
    catalogo_libros, prestamos_libros = registrar_prestamo(
        catalogo_libros, prestamos_libros, "4", "2"
    )
    print_prestamos(prestamos_libros)

    print("\n")

    print("Pregunta 6: Registrar Devolucion" + "\n")
    print("Catalogo original")

    print_catalogo(catalogo_libros)
    print_prestamos(prestamos_libros)

    (
        catalogo_libros,
        prestamos_libros,
    ) = registrar_devolucion(
        catalogo_libros, catalogo_libros_original, prestamos_libros, "3", "11"
    )
    print("Catalogo actualizado")
    print_catalogo(catalogo_libros)
    print("Prestamos actualizado")
    print_prestamos(prestamos_libros)

    # print(registrar_devolucion('prestamos.txt', '2', '1'))
    # print(registrar_devolucion('prestamos.txt', '67', '1'))

    guardar_catalogo("catalogo_actualizado.txt", catalogo_libros)
    guardar_prestamos("prestamos_actualizado.txt", prestamos_libros)


demo()
