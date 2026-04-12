# === SISTEMA DE ALERTAS AMPLIADO ===

temperatura = float(input("Temperatura (°C): "))
humedad = float(input("Humedad (%): "))
luz = float(input("Horas de luz: "))

alertas = 0

if temperatura > 35:
    print("ALERTA: Temperatura demasiado alta. Activar ventilación.")
    
if temperatura < 10:
    print("ALERTA: Temperatura demasiado baja. Activar calefacción.")
    
if humedad > 80:
    print("ALERTA: Humedad excesiva. Riesgo de hongos.")
    
if humedad < 30:
    print("ALERTA: Humedad muy baja. Activar riego por aspersión.")

if luz < 4:
    print("ALERTA: Luz insuficiente. Encender lámparas de cultivo.")

if luz > 14:
    print("ALERTA: Exceso de luz. Cerrar cortinas del invernadero.")
