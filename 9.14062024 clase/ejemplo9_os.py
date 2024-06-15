import os
import prog1

prog1.titulo("Directorio actual con os.getcwd()")
print("  " + os.getcwd())

prog1.titulo("Uso os.chdir()")

print("Un nivel más arriba 👆")
os.chdir("..")
print(os.getcwd())
os.chdir("..")
print("Un nivel más arriba 👆")
print(os.getcwd())

prog1.titulo("Listar los archivos del directorio con os.getcwd()")
print(*os.listdir(), sep="\n")

prog1.titulo("Uso mkdir() para crear archivos")

os.chdir("C:\\")
if not os.path.exists("temp"):
    os.mkdir("temp")
os.chdir("temp")

file = open("test.txt", "wt", encoding="utf8")
file.write("Empiece a escribir aquí!\n")
file.close()

prog1.titulo("Uso de startfile para abrir aplicación asociada con archivo")
os.startfile(os.path.join("C:", "temp", "test.txt"))
