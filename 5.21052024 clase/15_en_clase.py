def imprimir_invitados(lista):
    print(len(lista), "personas:")
    for n in lista:
        print("*", n)
    
invitados = ["Martín", "Cristian", "Tomás", "Mateo", "Yamila"]
nombre = input("Ingrese el nombre del invitado (fin para terminar):")
while nombre.lower() != "fin":
    invitados.append(nombre)
    nombre = input("Ingrese el nombre del invitado (fin para terminar):")

print("Invitados antes de filtrar")
imprimir_invitados(invitados)

if ("Nacho" in invitados):
    print("Nacho no va porque es un aburrido!")
    invitados.remove("Nacho")

print("Invitados después de filtrar")
imprimir_invitados(invitados)
    
print(len(invitados), "por orden alfabético:")    
invitados.sort()
imprimir_invitados(invitados)