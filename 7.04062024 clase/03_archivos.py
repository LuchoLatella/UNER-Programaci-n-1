# Este programa abre y cierra un archivo.
# Si el archivo no existe => lo crea
obj_archivo = open('prog1.txt', 'wt')
obj_archivo.close()


# Si ejecutamos estas dos instrucciones que siguen y el archivo no existe tendremos un error.
# obj_archivo = open('prog1.txt', 'rt')
# obj_archivo.close()