#Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al 
#derecho que al revés. Por ejemplo: rayar, kayak, somos.

texto = input ("Ingrese el texto a verificar si es palíndromo: ").upper()
palindromo = texto == texto [::-1]

if palindromo:
    print("El texto " + texto + " es un palíndromo")
else:
    print ("El texto " + texto + " no es un palíndromo")

#print ("Los textos son: " , texto , "y" , palindromo)