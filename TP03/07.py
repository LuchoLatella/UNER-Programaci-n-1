# Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
# con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
# usuario:
# a. Agregar nuevas tareas pendientes.
# b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
# de la lista de pendientes a la de terminadas.
# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
# listas

def mostrar_menu():
    print("Opciones:")
    print("1. Agregar nueva tarea pendiente")
    print("2. Marcar tarea pendiente como terminada")
    print("3. Mostrar listas de tareas")
    print("4. Salir")

def agregar_tarea_pendiente(tareas_pendientes):
    tarea = input("Ingrese la nueva tarea pendiente: ")
    tareas_pendientes.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista de pendientes.")

def marcar_tarea_terminada(tareas_pendientes, tareas_terminadas):
    if not tareas_pendientes:
        print("No hay tareas pendientes para marcar como terminadas.")
        return
    
    print("Tareas pendientes:")
    for idx, tarea in enumerate(tareas_pendientes, start=1):
        print(f"{idx}. {tarea}")
    
    try:
        numero = int(input("Ingrese el número de la tarea que desea marcar como terminada: "))
        if 1 <= numero <= len(tareas_pendientes):
            tarea_terminada = tareas_pendientes.pop(numero - 1)
            tareas_terminadas.append(tarea_terminada)
            print(f"Tarea '{tarea_terminada}' marcada como terminada y movida a la lista de terminadas.")
        else:
            print("Número inválido. Por favor, intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

def mostrar_listas(tareas_pendientes, tareas_terminadas):
    print("\nTareas pendientes:")
    if tareas_pendientes:
        for tarea in tareas_pendientes:
            print(f"- {tarea}")
    else:
        print("No hay tareas pendientes.")
    
    print("\nTareas terminadas:")
    if tareas_terminadas:
        for tarea in tareas_terminadas:
            print(f"- {tarea}")
    else:
        print("No hay tareas terminadas.")

def mostrar_tareas():
    tareas_pendientes = []
    tareas_terminadas = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea_pendiente(tareas_pendientes)
        elif opcion == '2':
            marcar_tarea_terminada(tareas_pendientes, tareas_terminadas)
        elif opcion == '3':
            mostrar_listas(tareas_pendientes, tareas_terminadas)
        elif opcion == '4':
            print("Saliendo del programa / tareas terminadas.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

mostrar_tareas()