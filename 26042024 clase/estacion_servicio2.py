#print ("Ingrese el nombre del operario: ")
nombre_operador = input("Bienvenido, ingrese el nombre del operario: ")
print ("Hola operador " + nombre_operador + ", el sistema está listo.")
precio_x_litro = float (input ("Ingresar el precio por litro: "))
print ("El precio por litro es: ", precio_x_litro)

def ingresar_litros_vendidos(nombre_surtidor):
    litros_vendidos = float(input (f"La cantidad de litros vendidos en surtidor  {nombre_surtidor}: "))
    print (f"surtidor : {nombre_surtidor} : {litros_vendidos}")
    return litros_vendidos

def recaudacion_por_surtidor(identificador_surtidor, cantidad_litros):
    resultado = cantidad_litros * precio_x_litro
    print ("Surtidor ", identificador_surtidor, " - litros: ", cantidad_litros, " - resultado ", resultado)
    return resultado

surtidor_1 = ingresar_litros_vendidos(1)
surtidor_2 = ingresar_litros_vendidos(2)
surtidor_3 = ingresar_litros_vendidos(3)

resultado_1 = recaudacion_por_surtidor(1, surtidor_1)
resultado_2 = recaudacion_por_surtidor(2, surtidor_2)
resultado_3 = recaudacion_por_surtidor(3, surtidor_3)

litros_vendidos = surtidor_1 + surtidor_2 + surtidor_3
recaudacion_total = resultado_1 + resultado_2 + resultado_3
print("Cantidad de litros vendidos: ", litros_vendidos)
print("Cantidad de dinero recaudado: ", recaudacion_total)

promedio_litros_vendiddos = litros_vendidos/3
print("El promedio de litros vendidos en el día es: ", promedio_litros_vendiddos)



#print ("Surtidor 1 :", surtidor_1)
#print ("Surtidor 2 : ", surtidor_2)
#print ("Surtidor 3 : ", surtidor_3)
#resultado_1 = surtidor_1 * precio_x_litro
#resultado_2 = surtidor_2 * precio_x_litro
#resultado_3 = surtidor_3 * precio_x_litro
#print ("En total fué: litros" , surtidor_1 , "Recaudado: " , resultado_1)
#print ("En total fué: litros" , surtidor_2 , "Recaudado: " , resultado_2)
# ("En total fué: litros" , surtidor_3 ,"Recaudado: " , resultado_3)

#litros_vendidos = surtidor_1 + surtidor_2 + surtidor_3
#recaudacion_total = resultado_1 + resultado_2 + resultado_3
#print ("Cantidad de litros vendidos: ", litros_vendidos)
#print ("Dinero total recaudado:", recaudacion_total)