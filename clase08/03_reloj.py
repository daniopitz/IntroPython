hora = 0
while hora < 24:
    minuto = 0
    while minuto < 60:
        if hora < 10:
            h='0'+str(hora)
        else:
            h=str(h)
        if minuto < 10:
            m= '0'+str(minuto)
        else:
            m= str(minuto)
        print(h + ":" + m)
        minuto = minuto + 1
    hora = hora + 1
