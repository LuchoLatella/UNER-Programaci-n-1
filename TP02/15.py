# Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
# validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
# informarle que no se puede procesar el dato.

def vocales(letra_usuario):
    vocales = "aeiouAEIOU"
    return letra_usuario in vocales

def tipo_letra():
    letra_usuario = input("Ingrese una letra: ")

    if len(letra_usuario) != 1:
        print("No se puede procesar el dato ingresado...")
    else:
        if vocales(letra_usuario):
            print("es vocal")
        else:
            print("no es vocal")

tipo_letra()
    

    

    #letra_usuario = input("Ingrese una letra: ")
