# Mutaciones
# Modificación de un elemento
frutas = ["ananá", "banana", "manzana"]
print("frutas:", frutas)

frutas[0] = "pera"
frutas[-1] = "naranja"

print("frutas:", frutas)

# Modificación de varios elementos con slice
lista = ['a', 'b', 'c', 'd', 'e', 'f']
print("lista: ", lista)
lista[1:3] = ['x', 'y']
print(lista)

# Elimninación de elementos con slice y lista vacía
lista = ['a', 'b', 'c', 'd', 'e', 'f']
print("lista: ", lista)
lista[1:3] = []
print("lista: ", lista)