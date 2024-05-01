def dibujar_a():
    print ('a ' * multiplo)

def dibujar_b():
    print ('b ' * multiplo)

def dibujar_c():
    print ('c ' * multiplo)

def dibujar(letra):
    print (letra * 30)

multiplo = 30
opcion = input('Ingrese una letra: ')

if opcion == 'a':
    dibujar_a()
elif opcion == 'b':
    dibujar_b()
elif opcion == 'c':
    dibujar_c()
else:
    dibujar(opcion)