import random
import prog1

prog1.titulo("random.randint()")

for i in range(0, 10):
    print("Aleatorio:", random.randint(1, 10))
    
prog1.titulo("random.choices()")
    
comidas = ["Pizza", "Empanadas", "Hamburguesa", "Sorrentinos", "Ravioles", "Milanesa"]    
print("Voy a comer: ", end="")
print(*random.choices(comidas), sep=" y ")
print("Voy a comer: ", end="")
print(*random.choices(comidas, k=2), sep=" y ")
print("Voy a comer: ", end="")
print(*random.choices(comidas, k=3), sep=" y ")

prog1.titulo("random.shuffle()")

comidas_del_dia = ["Desayuno", "Almuerzo", "Merienda", "Cena"]
print("Comidas del día: ", end="")
print(*comidas_del_dia, sep=", ")
random.shuffle(comidas_del_dia)
print("Comidas del día: ", end="")
print(*comidas_del_dia, sep=", ")