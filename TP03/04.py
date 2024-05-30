# Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
# realizar lo siguiente:
# a. Imprimir la cantidad de elementos que tiene la lista.
# b. Imprimir el primer y último elemento.
# c. Imprimir el resto.
# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
# la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
# la lista. Quitar el elemento correspondiente de esa posición.
# f. Imprimir la lista en orden inverso.
# g. Vaciar la lista.

paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

#a.
print(f"Cantidad de ítems en países es:",len(paises))
#b.
print(f"Primer país de la lista es {paises[0]}, el último es {paises[-1]}")
#c.
print(f"Resto de los países: {paises[1:-1]}")
#d.
pais_usuario = input("Por favor, ingrese un país: ")

if pais_usuario in paises:
    indice = paises.index(pais_usuario)
    print(f"El país '{pais_usuario}' se encuentra en la lista en el índice {indice}.")
else:
    print(f"El país '{pais_usuario}' no se encuentra en la lista.")