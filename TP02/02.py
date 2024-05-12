# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado

def calculo_pontecia (entero,potencia):
    if entero <= 0:
        return "Intente nuevamente con un número entero positivo"
    else: resultado = entero ** potencia 
    return resultado

entero = int(input ("Ingrese un número entero: "))
potencia = int(input ("ingrese una potencia :"))

resultado = calculo_pontecia(entero,potencia)
print(f"El resultado de", entero, "elevado a la potencia", potencia , "es:", resultado)
