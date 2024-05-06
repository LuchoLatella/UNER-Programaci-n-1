#operario = input("Ingresar el nombre del operario: ")
precio_litro_nafta = 0
total_ejecucion_por_corte = 3
acumulador = 0
#TODO: Pasar esto a una funcion porque seguramente vamos a tener que revisar en otros ingresos si lo que ingresa la persona es un caracter o numero.

while precio_litro_nafta == 0 and acumulador < total_ejecucion_por_corte :
    acumulador = acumulador + 1 
    print(f'acumulador { acumulador}')
    print("Si quiere salir del sistema ingrese SALIR o  ingrese el precio del litro de nafta para continuar!!")
    valor_de_entrada = input("Ingresar el precio del litro de nafta: ")
    if valor_de_entrada == "SALIR":
        exit()
    else:
        #TODO: ARREGLAR ESTO! Debe soportar enteros y floats. Try and catch como ejemplo
        if valor_de_entrada.isdigit() != True or valor_de_entrada.isnumeric():
            continue
        var_casteada = float(valor_de_entrada)
        if(var_casteada > 0):
            precio_litro_nafta = var_casteada
            break
    
print(precio_litro_nafta)