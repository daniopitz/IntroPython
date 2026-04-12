# === SISTEMA DE ALERTAS AMPLIADO CON elif ===

temperatura = float(input("Temperatura (°C): "))
humedad = float(input("Humedad (%): "))
luz = float(input("Horas de luz: "))

# Sensor de temperatura (alta o baja, nunca ambas)
if temperatura > 35:
    print("ALERTA: Temperatura demasiado alta. Activar ventilación.")
elif temperatura < 10:
    print("ALERTA: Temperatura demasiado baja. Activar calefacción.")

# Sensor de humedad (alta o baja, nunca ambas)
if humedad > 80:
    print("ALERTA: Humedad excesiva. Riesgo de hongos.")
elif humedad < 30:
    print("ALERTA: Humedad muy baja. Activar riego por aspersión.")

# Sensor de luz (exceso o falta, nunca ambas)
if luz < 4:
    print("ALERTA: Luz insuficiente. Encender lámparas de cultivo.")
elif luz > 14:
    print("ALERTA: Exceso de luz. Cerrar cortinas del invernadero.")
