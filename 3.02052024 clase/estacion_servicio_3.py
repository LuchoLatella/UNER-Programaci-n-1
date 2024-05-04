operario = input ("Ingrese el nombre del operario: ")

precio_litro_nafta = 0
total_ejecucion_corte = 3
acumulador = 0

while precio_litro_nafta == 0 or acumulador <= total_ejecucion_corte :
    print ("Ingrese el valor del litro de nafta o si desea salir del sistema?? presione S: ")
    valor_de_entrada = input ("Ingrese el valor del litro de nafta: ")
    if valor_de_entrada == "S":
        exit()
    else:
        variable_casteada = float(valor_de_entrada)
        if (variable_casteada > 0):
            precio_litro_nafta = variable_casteada
            break
        acumulador = acumulador + 1
        print(f'acumulador+{acumulador}')

print(precio_litro_nafta)