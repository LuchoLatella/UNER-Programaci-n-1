print ('Menú principal')
print ('===============')
print ('1. Clientes')
print ('2. Proveedores')
print ('3. Empleados')
print ()
menu = int(input('Seleccione una opción: '))
match menu:
    case 1: 
        print("** Seleccionó Clientes")
    case 2:
        print("** Seleccionó Proveedores")
    case 3:
        print("** Seleccionó Empleados")
    case _:
        print("** Seleccionó una opción no válida")