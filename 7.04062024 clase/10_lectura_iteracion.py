cadena = ''
obj_archivo = open('jugadores-liverpool.txt', 'rt', encoding='utf-8')
for linea in obj_archivo:
    cadena += linea
obj_archivo.close()
print("cadena:", cadena)
print("longitud:", len(cadena))