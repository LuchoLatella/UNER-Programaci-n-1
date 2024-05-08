# Que dada la base y altura de un triángulo nos calcule su área.

def calculo_area_tirangulo(base, altura):
    area_triangulo = (base * altura)/ 2
    return area_triangulo

usuario = input("Por favor, ingrese su nombre: ")
base = float(input("Usuario " + usuario + ", ingrese la base del triángulo: "))
altura = float(input ("ingrese la altura del triángulo :"))

area_triangulo = calculo_area_tirangulo(base,altura)

print(f"El área del triángulo seleccionado es",area_triangulo)