# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def definir_edad():
    edad = int(input("Ingrese la edad :"))
    mayor_menor = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
    return(mayor_menor)

mayor_menor = definir_edad()   
print(mayor_menor)