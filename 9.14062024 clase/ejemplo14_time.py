import time
import random
import prog1

def ordenacion(lista):
    for i, i_valor in enumerate(lista):
        for j, j_valor in enumerate(lista):
            if i_valor < j_valor:
                aux = lista[i]
                lista[i] = j_valor
                lista[j] = aux

prog1.titulo("time.time()")
print("time.time():", time.time())

limite_max = 10000

lista = []
for i in range(0, limite_max):
    lista.append(random.randint(0, 100))
    
lista2 = []
for i in range(0, limite_max):
    lista2.append(random.randint(0, 100))
    
prog1.titulo("ordenación y medición de tiempo con time()")

inicio = time.time()
ordenacion(lista)
tiempo = time.time() - inicio
print("tiempo:", tiempo, "en segundos")

prog1.titulo("ordenación con sort() y medición de tiempo con time()")
inicio = time.time()
lista2.sort()
tiempo = time.time() - inicio

print("tiempo:", tiempo, "en segundos")