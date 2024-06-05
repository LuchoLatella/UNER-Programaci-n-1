cadena = ''
obj_archivo = open('jugadores-liverpool.txt', 'rt', encoding='utf-8')
while True:
    linea = obj_archivo.readline()
    if not linea:
        break
    cadena += linea
obj_archivo.close()
print("cadena:", cadena)
print('longitud:', len(cadena))