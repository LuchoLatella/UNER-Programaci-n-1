# Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#a. Todos los números impares desde 1 hasta ese número separados por comas.
#b. La cuenta atrás desde ese número hasta cero separados por comas.
#c. Que indique si es primo o no.
#d. Por último, su factorial.

def num_impares(numero):
    impares = ""
    for n in range(1,numero+1,2):
        if n == 1:
            impares += str(n)
        else:
            impares += ", " + str(n)
    return impares
            
#def num_impares(numero):
#    impares = [str(n) for n in range(1, numero + 1, 2)]
#    return ", ".join(impares)

def cuenta_atras(numero):
    countdown = [str(n) for n in range(numero, -1, -1)]
    return ", ".join(countdown)

def es_primo(numero):
    if numero <= 1:
        return False
    for n in range(2, int(numero**0.5) + 1):
        if numero % n == 0:
            return False
    return True

def calculo_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calculo_factorial(numero - 1)

def resultado():
    num_usuario = int(input("Ingrese un numero entero positivo: "))

    impares = num_impares(num_usuario)
    print(f"Números impares desde 1 hasta {num_usuario}: {impares}")

    cuenta_regresiva = cuenta_atras(num_usuario)
    print(f"Cuenta atrás desde {num_usuario} hasta 0: {cuenta_regresiva}")

    if es_primo(num_usuario):
        print(f"{num_usuario} es un número primo")
    else:
        print(f"{num_usuario} no es un número primo")
    
    factor = calculo_factorial(num_usuario)
    print(f"factorial de {num_usuario} es {factor}")

resultado()