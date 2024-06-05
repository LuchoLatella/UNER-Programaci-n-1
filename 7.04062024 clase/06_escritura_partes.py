cadena = """Édouard Mendy
Antonio Rüdiger
Andreas Christensen
Thiago Silva
Reece James
Marcos Alonso
Jorginho
N'Golo Kanté
Mason Mount
Kai Havertz
Romelu Lukaku"""
obj_archivo = open('jugadores-chelsea.txt', 'wt', encoding='utf-8')
longitud = len(cadena)
desplazamiento = 0
tamanio_parte = 20
while True:
    if desplazamiento > longitud:
        break
    obj_archivo.write(cadena[desplazamiento:desplazamiento+tamanio_parte])
    desplazamiento += 20
obj_archivo.close()