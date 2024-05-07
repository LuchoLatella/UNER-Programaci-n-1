# Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
 

def calculo_factura_iva(importe_factura,iva):
    factura_final = importe_factura + importe_factura * (iva / 100)
    return factura_final

importe_factura = float(input ("Ingrese el valor de la factura : "))
iva = float(input("Ingrese el porcentaje de IVA a aplicar (por defecto 21%): ") or 21)   

total_factura = calculo_factura_iva(importe_factura,iva)

print(f"El total de la factura con el",iva,"% de IVA, es:",total_factura)




