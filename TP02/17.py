#Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_numero_primos(minimo, maximo):
    primos = [numero for numero in range(minimo, maximo + 1) if es_primo(numero)]
    print(f"Números primos entre {minimo} y {maximo}: {primos}")
    print(f"Hay {len(primos)} números primos entre {minimo} y {maximo}.")


mostrar_numero_primos(0, 100)