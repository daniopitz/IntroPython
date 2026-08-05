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





print(obtener_total("Chile;Concepción;13456;Valparaíso;13456;Santiago;17893"))
