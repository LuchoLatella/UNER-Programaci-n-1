# Que dado tres números ingresados por el usuario nos devuelva el promedio.

def obtener_promedio(numero1,numero2,numero3):
    promedio = (numero1 + numero2 + numero3)/ 3
    return promedio
    
numero1 = float(input("Ingrese el primer número :"))
numero2 = float(input("Ingrese el segundo número :"))
numero3 = float(input("Ingrese el tercer número :"))    

calculo_promedio = obtener_promedio(numero1,numero2,numero3)

print(f"El promedio de los tres números dados es: ", calculo_promedio)