cadena = ''
obj_archivo = open('jugadores-liverpool.txt', 'rt', encoding='utf-8')
tamanio_parte = 100
while True:
    fragmento = obj_archivo.read(tamanio_parte)
    if not fragmento:
        break
    cadena += fragmento
obj_archivo.close()
print("cadena:", cadena)
print("longitud:", len(cadena))