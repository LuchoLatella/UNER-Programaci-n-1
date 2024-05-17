# Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
# múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
# ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
# no es bisiesto

def definir_bisiesto(anio_usuario):
    if anio_usuario % 4 == 0 and anio_usuario % 100 != 0 or anio_usuario % 400 == 0:
        return True
    else:
        return False
    
def es_bisiesto():
    anio_usuario = int(input("Por favor ingrese el año: "))
    if definir_bisiesto(anio_usuario):
        print(f"{anio_usuario} es bisiesto")
    else:
        print(f"{anio_usuario} no es bisiesto")

es_bisiesto()