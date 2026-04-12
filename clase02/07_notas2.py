nota1 = float(input("Ingrese nota del primer certamen (0-100): "))
nota2 = float(input("Ingrese nota del segundo certamen (0-100): "))
asistencia = float(input("Ingrese porcentaje de asistencia: "))

promedio = (nota1 + nota2) / 2

if promedio >= 55 and asistencia >= 75:
    print("Aprobado")
else:
    if promedio < 55 and asistencia < 75:
        print("Reprobado por nota y asistencia")
    else:
        if promedio < 55:
            print("Reprobado por nota")
        else:
            print("Reprobado por asistencia")
