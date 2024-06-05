import json

cadena = ''

with open('15_menu.json', 'r') as archivo:
    linea = archivo.readline()
    while linea: 
        cadena += linea
        linea = archivo.readline()
    
print(cadena)    

menu = json.loads(cadena)

print("menú:", menu)

print("menu['almuerzo']:", menu['almuerzo'])