import datetime

def es_dia_habil(fecha):
    """
    Comprueba si un día dado es hábil (lunes a viernes).
    """
    return fecha.weekday() < 5

def contar_dias_habiles(fecha_inicio, fecha_fin):
    """
    Cuenta la cantidad de días hábiles entre dos fechas.
    """
    dias_habiles = 0
    fecha_actual = fecha_inicio

    while fecha_actual <= fecha_fin:
        if es_dia_habil(fecha_actual):
            dias_habiles += 1
        fecha_actual += datetime.timedelta(days=1)

    return dias_habiles

def main():
    # Solicitar al usuario las fechas de inicio y fin
    nombre_usuario = input("Bienvenido, ingrese su nombre por favor: ")
    fecha_inicio_str = input("Ingrese la fecha de inicio (DD-MM-AAAA): ")
    fecha_fin_str = input("Ingrese la fecha de fin (DD-MM-AAAA): ")

    # Convertir las cadenas de texto a objetos de fecha
    fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
    fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%d-%m-%Y")

    # Calcular la cantidad total de días
    total_dias = (fecha_fin - fecha_inicio).days + 1

    # Contar días hábiles y no hábiles
    dias_habiles = contar_dias_habiles(fecha_inicio, fecha_fin)
    dias_no_habiles = total_dias - dias_habiles

    # Mostrar resultados
    print(nombre_usuario + ", la cantidad total de días es:", total_dias)
    print(nombre_usuario + ", la cantidad total de hábiles es:", dias_habiles)
    print(nombre_usuario + ", la cantidad total de no hábiles es:", dias_no_habiles)

if __name__ == "__main__":
    main()