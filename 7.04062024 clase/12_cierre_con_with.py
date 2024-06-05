cadena = """David De Gea
Diogo Dalot
Victor Lindelöf
Harry Maguire
Aaron Wan-Bissaka
Paul Pogba
Scott McTominay
Nemanja Matić
Bruno Fernandes
Cristiano Ronaldo
Edinson Cavani"""
with open('jugadores-man-utd.txt', 'wt', encoding='utf-8') as archivo_salida:
 	archivo_salida.write(cadena)
  
with open('jugadores-man-utd.txt', 'rt', encoding='utf-8') as archivo_entrada:
 	cadena_nueva = archivo_entrada.readlines()
  
print("cadena_nueva:", cadena_nueva)  