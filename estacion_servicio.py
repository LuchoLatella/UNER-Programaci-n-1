#print ("Ingrese el nombre del operario: ")
nombre_operador = input("Bienvenido, ingrese el nombre del operario: ")
print ("Hola operador " + nombre_operador + ", el sistema está listo.")
precio_x_litro = float (input ("Ingresar el precio por litro: "))
print ("El precio por litro es: ", precio_x_litro)
surtidor_1 = float(input ("La cantidad de litros vendidos en surtidor 1 es: "))
surtidor_2 = float(input ("La cantidad de litros vendidos en surtidor 2es: "))
surtidor_3 = float(input("La cantidad de litros vendidos en surtidor 3 es: "))
print ("Surtidor 1 :", surtidor_1)
print ("Surtidor 2 : ", surtidor_2)
print ("Surtidor 3 : ", surtidor_3)
resultado_1 = surtidor_1 * precio_x_litro
resultado_2 = surtidor_2 * precio_x_litro
resultado_3 = surtidor_3 * precio_x_litro
print ("En total fué: litros" , surtidor_1 , "Recaudado: " , resultado_1)
print ("En total fué: litros" , surtidor_2 , "Recaudado: " , resultado_2)
print ("En total fué: litros" , surtidor_3 ,"Recaudado: " , resultado_3)

litros_vendidos = surtidor_1 + surtidor_2 + surtidor_3
recaudacion_total = resultado_1 + resultado_2 + resultado_3
print ("Cantidad de litros vendidos: ", litros_vendidos)
print ("Dinero total recaudado:", recaudacion_total)