# Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
# de una lista vacía:
# a. Agregar un elemento al final.
# b. Agregar un elemento al principio.
# c. Quitar un elemento al final.
# d. Quitar un elemento al principio

def mostrar_menu():
    print("Opciones:")
    print("1. Agregar un elemento al final")
    print("2. Agregar un elemento al principio")
    print("3. Quitar un elemento al final")
    print("4. Quitar un elemento al principio")
    print("5. Mostrar lista")
    print("6. Salir")

def agregar_al_final(lista):
    elemento = input("Ingrese el elemento a agregar al final: ")
    lista.append(elemento)
    print(f"'{elemento}' agregado al final de la lista.")

def agregar_al_principio(lista):
    elemento = input("Ingrese el elemento a agregar al principio: ")
    lista.insert(0, elemento)
    print(f"'{elemento}' agregado al principio de la lista.")

def quitar_del_final(lista):
    if lista:
        elemento = lista.pop()
        print(f"'{elemento}' quitado del final de la lista.")
    else:
        print("La lista está vacía, no se puede quitar elementos.")

def quitar_del_principio(lista):
    if lista:
        elemento = lista.pop(0)
        print(f"'{elemento}' quitado del principio de la lista.")
    else:
        print("La lista está vacía, no se puede quitar elementos.")

def mostrar_lista(lista):
    print("Lista actual:", lista)

def interaccion_con_lista():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Por favor, seleccione una opción: ")

        if opcion == '1':
            agregar_al_final(lista)
        elif opcion == '2':
            agregar_al_principio(lista)
        elif opcion == '3':
            quitar_del_final(lista)
        elif opcion == '4':
            quitar_del_principio(lista)
        elif opcion == '5':
            mostrar_lista(lista)
        elif opcion == '6':
            print("Ha salido del sistema.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

interaccion_con_lista()