# Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado


numeros_usuario = []
for i in range(5):
    numero = int(input(f"Por favor, ingrese el número {i+1}: "))
    numeros_usuario.append(numero)

ordenar_numeros = sorted(numeros_usuario)

print("Los números elegidos quedan ordenados así:", ordenar_numeros)