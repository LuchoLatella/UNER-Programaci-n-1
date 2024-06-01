# Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
# usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
# de los números ingresados por el usuario deberá ser almacenado en una lista. A
# continuación, realice las siguientes tareas:
# a. Determinar el máximo.
# b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
# c. Determinar el mínimo.
# d. Calcular la multiplicación de todos los números de la lista.
# e. Contar los valores pares e impares.
# f. Remover los elementos repetidos.

def numeros_usuario():
    numeros = []

    while True:
        numeros_usuario = (input("Por favor ingrese un número, para finalizar presione - fin -: "))
        if numeros_usuario == "fin":
            print("Presionado FIN, termina la secuencia.")
            break
        try:
            numero = int(numeros_usuario)
            numeros.append(numero)
            print("se agregó el número:",numero)
        except ValueError:
            print("Ingreso no válido, intente nuevamente un número entero...")
    return numeros

    numeros_usuario != "FIN":
        
   