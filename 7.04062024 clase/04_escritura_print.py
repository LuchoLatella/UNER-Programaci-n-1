# Este programa abre un archivo (prog1.txt) si no existe lo crea y 
# escribe el texto que figura en la función print.
# Ver qué pasa si lo ejecutamos muchas veces

obj_archivo = open('prog1.txt', 'wt')
print('Vamooo!!! Cree un archivo (con print)', file=obj_archivo)
obj_archivo.close()