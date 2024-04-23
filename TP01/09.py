# Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

nombre = input ("Ingrese su nombre: ")
texto_usuario = input ("Por favor, " + nombre + " ingrese el texto deseado: ")
print (texto_usuario [::-1])