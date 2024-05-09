# Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#a. Todos los números impares desde 1 hasta ese número separados por comas.
#b. La cuenta atrás desde ese número hasta cero separados por comas.
#c. Que indique si es primo o no.
#d. Por último, su factorial.

def num_impares(numero):
    for n in range(1, numero+1, 2):
        return ", ".join(num_impares)

def cuenta_atras(numero):
    while numero > 0:
        numero = numero -1
        return ", ".join(cuenta_atras)

def es_primo(numero):
    for n in range(2, int(numero**0.5) + 1):
        if numero % n == 0:
            return False
        return True
    
def calculo_factorial(numero):
    factorial = numero * factorial(numero-1)
    return factorial

def resultado():
    num_usuario = int(input( "Ingrese un numero entero positivo: "))

    impares = num_impares(num_usuario)
    print(f"Números impares desde 1 hasta´{impares}: {impares}")

    cuenta_regresiva = cuenta_atras(num_usuario)
    print(f"Cuenta atrás desde {num_usuario} hasta 0 {cuenta_regresiva}")

    if es_primo(num_usuario):
        print(f"{num_usuario} es un número primo")
    else:
        print(f"{num_usuario} no es un número primo")
    
    factor = calculo_factorial(num_usuario)
    print(f"factorial de {num_usuario} es {factor}")

mostrar_resultado = resultado()
print(mostrar_resultado)
