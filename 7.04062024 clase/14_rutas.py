import os

obj_archivo = open('prog1.txt', 'r')
print(obj_archivo.readlines())

print("os.path.abspath('prog1.txt'):", os.path.abspath('prog1.txt'))

obj_archivo = open('C:\prog1.txt', 'r')
print(obj_archivo.readlines())

obj_archivo = open('.\\subcarpeta\\prog1.txt')
print(obj_archivo.readlines())

ruta = os.path.join('.', 'subcarpeta', 'prog1.txt')
print("ruta:", ruta)
obj_archivo = open(ruta)
print(obj_archivo.readlines())