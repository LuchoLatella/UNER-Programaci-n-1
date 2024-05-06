#Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

def saludo_inicial (nombre_usuario):
    print (f"¡Hola {nombre_usuario}!")

ingreso_nombre = input ("Bienvenido, ingrese su nombre: ")

saludo_inicial(ingreso_nombre)