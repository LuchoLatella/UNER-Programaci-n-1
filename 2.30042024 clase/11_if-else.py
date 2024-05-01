numero = int(input('Ingrese un número (para determinar si es par o impar): '))
if numero % 2 == 0:
    print (numero, 'es par')
    print ('otra línea dentro de if')
else:
    print (numero, 'es impar')
    print ('otra línea dentro de else')

print('Fin')