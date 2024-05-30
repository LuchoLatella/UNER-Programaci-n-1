# Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
# frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
# debajo la misma lista pero sólo con las frutas que añadió el usuario.

frutas = ["banana", "manzana", "pera"]
frutas_agregadas = []

for i in range(3):
    frutas_usuario = input(f"Por favor, ingrese su fruta {i+1}: ")
    frutas_agregadas.append(frutas_usuario)
    frutas.append(frutas_usuario)
    

print(frutas)
print(frutas_agregadas)
