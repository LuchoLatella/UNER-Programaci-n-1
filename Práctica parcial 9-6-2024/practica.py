# EJERCICIO1) Escribir un programa Python que calcule el índice de masa corporal de una persona 
# (IMC).  

# Muestre por pantalla el estado en el que se encuentra esa persona en función del valor de IMC: 

peso = int(input("ingrese el peso a considerar: "))
altura = float(input("por favor, ingrese la altura a considerar: "))

def calculo_imc (peso, altura):
    imc = peso / altura**2
    print("El IMC de la persona es ", imc)

calculo_imc(peso, altura)


