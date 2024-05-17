# Que imprima el siguiente patrón:

def imprimir_el_patron(n):
    for i in range(n,0,-1):
     for j in range(i,0,-1):    
        print(j, end= " ")
     print()

imprimir_el_patron(5)