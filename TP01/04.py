# Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en pantalla: “La respuesta es XX”.

nombre = input ("Ingrese su nombre: ")
numero_1 = float(input ("Bienvenido " + nombre + ", ingrese un número: " ))
numero_2 = float(input ("Ingrese otro número por favor: "))
resultado_suma = numero_1 + numero_2
print (nombre + ", la suma de ambos números, es " , resultado_suma)