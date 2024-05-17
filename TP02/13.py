# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
# resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
# el grupo que le corresponde.


def definir_grupo(nombre,sexo):
    nombre = nombre.lower()

    if sexo.lower() == "f" and nombre <= "m":
        return "A"
    elif sexo.lower() == "m" and nombre >=  "n":
        return "A"
    else:
        return "B"

def elegir_grupo():
    nombre = input("Ingrese el nombre: ")
    sexo = input("por favor, ingrese el sexo (m/f): ")

    grupo = definir_grupo(nombre,sexo)
    print(f"Tu grupo es: {grupo}")
          
elegir_grupo()


