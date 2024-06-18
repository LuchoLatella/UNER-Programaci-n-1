
#  Para convertir entre las diferentes escalas de temperaturas Celsius (ºC), Fahrenheit 
# (ºF) se realizan los siguientes cálculos:
# • De ºC a ºF: se multiplica por 1,8 y se suma 32. 
# • De ºF a ºC: se resta 32 y se divide entre 1,8.
# Escribir un programa Python con dos funciones para permitir la conversión de escalas:
# convertir_celsius_fharenhait()
# convertir_fharenhait_celsius() 
# 1
 
# Mostrar la conversión de 53C°
# Mostrar la conversión de 77F°

def convertir_celsius_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def convertir_fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

# Conversión de 53 ºC a ºF
celsius = 53
fahrenheit = convertir_celsius_fahrenheit(celsius)
print(f"{celsius} ºC es igual a {fahrenheit:.2f} ºF")

# Conversión de 77 ºF a ºC
fahrenheit = 77
celsius = convertir_fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} ºF es igual a {celsius:.2f} ºC")

temperatura = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala a la que desea convertir (F para Fahrenheit, C para Celsius): ").upper()

if escala == 'F':
    resultado = convertir_celsius_fahrenheit(temperatura)
    print(f"{temperatura} ºC es igual a {resultado:.2f} ºF")
elif escala == 'C':
    resultado = convertir_fahrenheit_celsius(temperatura)
    print(f"{temperatura} ºF es igual a {resultado:.2f} ºC")
else:
    print("Escala no válida. Por favor ingrese 'F' para Fahrenheit o 'C' para Celsius.")