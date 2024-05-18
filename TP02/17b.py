#Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:
            return False
    return True

def mostrar_numero_primos():
    minimo = int(input("Ingrese el valor mínimo: "))
    maximo = int(input("Ingrese el valor máximo: "))  # modificado para que se solicite dos variables y las mida
    primos = [numero for numero in range(minimo, maximo + 1) if es_primo(numero)]
    print("Números primos entre", minimo, "y", maximo, ":", primos)
    print(f"Hay {len(primos)} números primos entre {minimo} y {maximo}.")

mostrar_numero_primos()