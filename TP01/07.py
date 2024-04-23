# Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y segundos son esos números de días.

nombre_1 = input ("Ingrese su nombre por favor: ")
dias_usuario = int(input ("Binevenido " + nombre_1 + ", ingrese la cantidad de días: "))
cantidad_horas = dias_usuario * 24
cantidad_minutos = cantidad_horas * 60
cantidad_segundos = cantidad_minutos * 60

print ("En total, señor " + nombre_1 + " han transcurrido " , cantidad_horas, "horas, ", cantidad_minutos, "minutos y ", cantidad_segundos, "segundos.-")