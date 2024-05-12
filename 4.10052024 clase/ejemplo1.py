
def conversor_pesos_dolares(importe_pesos, cotizacion):
    calculo_dolar = float(importe_pesos / cotizacion)
    return calculo_dolar

importe_pesos = float(input("Ingrese el valor en pesos argentinos : "))
cotizacion = float(input("Ingrese la cotización vendedor de BNA: "))

salida_en_dolares = conversor_pesos_dolares(importe_pesos,cotizacion)
print(f"El importe en dólares es: {salida_en_dolares}")