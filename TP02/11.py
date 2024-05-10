# Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se encuentran en dicha frase.

def contar_vocales(frase_usuario):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in frase_usuario:
        if caracter in vocales:
            contador += 1
    return contador

def vocales_encontradas():
    frase_usuario = input("Ingrese la frase a tomar en cuenta: ")
    cantidad_vocales = contar_vocales(frase_usuario)
    print(f"La cantidad de vocales encontradas es:", cantidad_vocales)

vocales_encontradas()