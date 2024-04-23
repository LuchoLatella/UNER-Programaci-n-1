# Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el 
# día,  mes y año. Ej:
# Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985

nombre = input ("Ingrese su nombre: ")
fecha = input (nombre + " ingrese la fecha en formato XX/XX/XXXX: ")

dia = fecha [0:2]
mes = fecha [3:5]
anio = fecha [6:10]

print ("Día: ", dia , ", mes: ",mes , " y año: ",anio)