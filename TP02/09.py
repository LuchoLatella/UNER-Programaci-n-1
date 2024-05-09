# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso en que ambos números son iguales.



def compara_numeros(numero1,numero2):
    if numero1 == numero2:
        return f"Ambos números son iguales",numero2
    elif numero1 > numero2:
        return f"El primer número",numero1,",es mayor que el segundo",numero2
    else:
        return f"El segundo número",numero2,"es mayor que el primero",numero1

def mostrar_comparacion():
    nombre_usuario = input("Ingrese su nombre de usuario :")
    numero1 = float(input("Por favor, " + nombre_usuario +" Ingrese el primer número :"))
    numero2 = float(input("Por favor, " + nombre_usuario + " Ingrese el segundo número :"))
    resultado = compara_numeros(numero1,numero2)
    return(resultado)

resultado = mostrar_comparacion()
print(resultado)

