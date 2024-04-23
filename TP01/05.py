# Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y 
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”.

nombre = input ("Ingrese su nombre: ")
numero_1 = float(input ("Bienvenido " + nombre + ", ingrese un número: " ))
numero_2 = float(input ("Ingrese otro número por favor: "))
resultado_suma = numero_1 + numero_2
print ("la suma de ambos números es: " , resultado_suma)
numero_3 = float(input ("Ingrese un tercer valor: "))
resultado_multi = resultado_suma * numero_3
print ("El resultado final de las dos operaciones es: " , resultado_multi)