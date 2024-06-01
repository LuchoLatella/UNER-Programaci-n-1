# Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
# muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

def mostrar_materias(materias):
    print("Lista de materias:")
    for materia in materias:
        print(f"- {materia}")

def lista_materias():
    materias = ["programación 1", "introducción a la informática", "diseño", "programación 2"]
    mostrar_materias(materias)
lista_materias()


