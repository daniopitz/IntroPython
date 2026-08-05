def pos(texto, c, p):
    i = 0
    j = 1
    while i < len(texto):
        if texto[i] == c:
            if j == p:
                return i
            j += 1
        i += 1
    return -1



def obtener_total(texto):
    # quitamos el país y agregamos ';' al final
    texto = texto[pos(texto, ";", 1) + 1:] + ";"
    
    total = 0
    n = 1  # empezamos en el 1er ';'
    
    p2 = pos(texto, ";", n + 1)

    while p2 != -1: #cuando no existe el segundo ';' paro
        p1 = pos(texto, ";", n)
        total += int(texto[p1 + 1:p2])
        n += 2
        p2 = pos(texto, ";", n + 1)
    
    return total


cantidad_paises = int(input("Ingrese la cantidad de países: "))

pais_max = ""
total_max = 0

i = 1
while i <= cantidad_paises:
    texto = input("Ingrese los datos del país: ")
    
    # extraemos el nombre del país (lo que está antes del primer ';')
    fin_pais = pos(texto, ";", 1)
    nombre_pais = texto[0:fin_pais]
    
    # calculamos el total de asistentes
    total = obtener_total(texto)
    
    print(nombre_pais, ":", total, "asistentes")
    
    # vamos guardando el país con más asistentes
    if total > total_max:
        total_max = total
        pais_max = nombre_pais
    
    i += 1

print("El país con más asistentes fue:", pais_max)
