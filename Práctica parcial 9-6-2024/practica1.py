# EJERCICIO1) Escribir un programa Python que calcule el índice de masa corporal de una persona 
# (IMC).  

# Muestre por pantalla el estado en el que se encuentra esa persona en función del valor de IMC: 



def calculo_imc (peso, altura):
    imc = peso / (altura**2)
    return imc    # print("El IMC de la persona es ", imc)

def estado_imc (imc):
    if imc < 18.5:
        return("Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        return("Normal")
    elif imc >= 25 and imc <= 29.9:
        return("Sobrepeso")
    elif imc >= 30 and imc <= 39.9:
        return("Obesidad")
    else:
        return("Obesidad morbida")


def mostrar_datos_imc():
    try:
        peso = float(input("ingrese el peso a considerar: "))
        altura = float(input("por favor, ingrese la altura a considerar: "))
    except ValueError:
        print("por favor, ingresar valores válidos")
        return

    imc = calculo_imc (peso, altura)
    
    print("El IMC de la persona es", imc)
    print("El estado de la persona es", estado_imc(imc))

mostrar_datos_imc()
# calculo_imc(peso, altura)


