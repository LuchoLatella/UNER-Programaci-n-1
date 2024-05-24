# Listas como parámetros de funciones
#Uso de listas como parámetros en funciones 
def cabeza(lista):
    return lista[0]

numeros = [1,2,3]
cabeza(numeros)

def funcion_con_int(y):
    y = 5
    print(y)

x = 83
print("x antes de la llamada a la función:", x)
funcion_con_int(x)
print("x después de la llamada a la función:", x)

def borra_cabeza(lista):
    del lista[0]

numeros = [1,2,3]
print("Antes de llamar a borra_cabeza() lista:", numeros)
borra_cabeza(numeros)
print("Después de llamar a borra_cabeza() lista:", numeros)