x = int(input('Ingrese un número: '))
y = int(input('Ingrese otro número: '))

if x == y:
    print(x, 'e', y, 'son iguales')
else:
    if x < y:
        print (x, 'es menor que', y)
    else:
        print(x, 'es mayor que', y)