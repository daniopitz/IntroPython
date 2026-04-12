# === SISTEMA DE ALERTAS - 4 SENSORES ===

temperatura = float(input("Temperatura (°C): "))
humedad = float(input("Humedad (%): "))
luz = float(input("Horas de luz: "))
co2 = float(input("Nivel de CO₂ (ppm): "))


alertas = 0

if temperatura > 35:
    print("ALERTA: Temperatura alta. Activar ventilación.")  

if humedad > 80:
    print("ALERTA: Humedad excesiva. Riesgo de hongos.")
  
if luz < 4:
    print("ALERTA: Luz insuficiente. Encender lámparas de cultivo.")

if co2 > 1000:
    print("ALERTA: CO₂ elevado. Ventilar el aire.")

