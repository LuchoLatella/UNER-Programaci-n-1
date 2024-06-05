# Este programa abre un archivo (prog1.txt) si no existe lo crea y 
# escribe el texto que figura en la función write.
# Ver qué pasa si lo ejecutamos muchas veces

obj_archivo = open('prog1.txt', 'wt')
obj_archivo.write('Vamooo!!! Cree un archivo (con write)')
obj_archivo.close()