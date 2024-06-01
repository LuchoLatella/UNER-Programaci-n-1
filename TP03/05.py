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

def determinar_maximo(lista):
    return max(lista)

def obtener_segundo_maximo(lista):
    maximo = max(lista)
    lista_sin_maximo = [x for x in lista if x != maximo]
    if not lista_sin_maximo:
        return None
    return max(lista_sin_maximo)

def determinar_minimo(lista):
    return min(lista)

def multiplicacion_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def contar_pares_impares(lista):
    pares = sum(1 for x in lista if x % 2 == 0)
    impares = len(lista) - pares
    return pares, impares

def remover_repetidos(lista):
    return list(set(lista))

def mostrar_todo():
    numeros = numeros_usuario()
    if not numeros:
        print("No se ingresaron números.")
        return

    maximo = determinar_maximo(numeros)
    segundo_maximo = obtener_segundo_maximo(numeros)
    minimo = determinar_minimo(numeros)
    multiplicacion = multiplicacion_lista(numeros)
    pares, impares = contar_pares_impares(numeros)
    sin_repetidos = remover_repetidos(numeros)

    print(f"Números ingresados: {numeros}")
    print(f"Máximo: {maximo}")
    if segundo_maximo is not None:
        print(f"Segundo máximo: {segundo_maximo}")
    else:
        print("No hay un segundo valor máximo.")
    print(f"Mínimo: {minimo}")
    print(f"Multiplicación de todos los números: {multiplicacion}")
    print(f"Cantidad de valores pares: {pares}")
    print(f"Cantidad de valores impares: {impares}")
    print(f"Lista sin elementos repetidos: {sin_repetidos}")

mostrar_todo()
        
   