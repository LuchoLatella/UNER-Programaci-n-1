# Métodos
#append() para agregar elementos
lista = ['a', 'b', 'c']
print("Antes de agregar 'd' a lista:", lista)
lista.append('d')
print("Después de agregar 'd' a lista:", lista)

lista = lista + ['e']
print("Después de agregar 'e' a lista:", lista)

#extend() para agregar a una lista todos los elementos de otra
t1 = ['a', 'b', 'c']
print("Antes de agregar todos los elementos de t2 a t1:", t1)
t2 = ['d', 'e']
print("Lista t2:", t2)
t1.extend(t2)
print("Después de agregar todos los elementos de t2 a t1:", t1)

#sort() ordena los elementos de una lista
t3 = ['4','3','2','1','d', 'c', 'e', 'b', 'B', 'a']
print("Antes ordenar los elementos de  t3:", t3)
t3.sort()
print("Después ordenar los elementos de  t3:", t3)
