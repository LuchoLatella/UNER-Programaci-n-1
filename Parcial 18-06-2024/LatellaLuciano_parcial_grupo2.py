
def temperatura_diaria_usuario():
    temperaturas = []

    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)

    temperaturas_ordenadas = sorted(temperaturas)
    print("\nTemperaturas ordenadas de menor a mayor:")
    print(temperaturas_ordenadas)

    promedio_temeperaturas = sum(temperaturas) / len(temperaturas)
    print(f"\nEl promedio de la temperatura de la semana es: {promedio_temeperaturas} °C.")

    temperaturas_cadena = ', '.join(map(str, temperaturas))
    print(f"\nTodas las temperaturas como cadena separadas por comas: {temperaturas_cadena}")

    dias_calurosos = 0
    for grados in temperaturas:
        if grados >= 24:
            dias_calurosos += 1
    
    print(f"\nCantidad de días con temperatura mayor o igual a 24 °C: {dias_calurosos}")




    
temperatura_diaria_usuario()
        
        
