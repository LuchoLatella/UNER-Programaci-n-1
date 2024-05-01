def imprimir_dos_veces(nombre):
    print(nombre)
    print(nombre)
    
def concat_imprimir(part1, part2):
    cat = part1 + part2
    imprimir_dos_veces(cat)
    print(cat + 'posterior')
    
linea1 = 'Línea 1 '
linea2 = 'Línea 2 '
concat_imprimir(linea1, linea2)

# print (cat) # arroja error