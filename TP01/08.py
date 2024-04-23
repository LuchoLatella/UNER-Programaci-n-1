# Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para luego imprimir por pantalla la superficie total.

nombre = input ("Ingrese su nombre: ")
base_triangulo = float(input ("Bienvenido " + nombre + ", ingrese el tamaño de la base: " ))
altura_triangulo = float(input ("Ingrese el valor de altura: "))

superficie_triangulo = (base_triangulo * altura_triangulo) / 2

print (nombre + ", la superficie del triángulo es: " , superficie_triangulo)