# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes,
# otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje

def solicitar_dia(dia_semana):
    if dia_semana.lower() == "lunes":
        return "es el día lunes, buena semana."
    elif dia_semana.lower() == "viernes":
        return "es el día viernes, buen descanso."
    elif dia_semana.lower() in ["sabado" , "domingo"]:
        return "disfrute, usted está en el fin de semana:"
    else:
        return "no se encuentra en uno de los días tenidos en cuenta."

def mensaje_dia_semana():
    dia_usuario = input("Por favor, ingrese el día de la semana: ")
    mensaje_salida = solicitar_dia(dia_usuario)
    print(mensaje_salida)

mensaje_dia_semana()