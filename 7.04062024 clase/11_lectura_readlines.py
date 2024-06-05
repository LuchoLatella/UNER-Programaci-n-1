obj_archivo = open('jugadores-liverpool.txt', 'rt', encoding='utf-8')
lineas = obj_archivo.readlines()
obj_archivo.close()
print("lista:", lineas)
print(len(lineas), 'líneas leídas')
for linea in lineas:
    # linea = linea.strip()
    print(linea, end="")