#Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

def saludo_inicial (nombre):
    print (f"¡Hola {nombre}!")

mostrar_nombre = input ("Bienvenido, ingrese su nombre: ")

saludo_inicial(mostrar_nombre)