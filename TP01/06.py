# Programe una aplicación de consola que pregunte  el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

nombre_1 = input ("Ingrese su nombre por favor: ")
total_cuenta = float(input ("Binevenido " + nombre_1 + ", ingrese el valor total de la cuenta: "))
comensales = int(input ("Cantidad de comensales que participaron: "))
costo_individuo = total_cuenta / comensales
print ("El costo a abonar por comensal es: " , costo_individuo)