
def temperatura_diaria_usuario():
    temperaturas = []

    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)

    temperaturas_ordenadas = sorted(temperaturas)
    print("\nTemperaturas ordenadas de menor a mayor:")
    print(temperaturas_ordenadas)

    promedio_temperaturas = sum(temperaturas) / len(temperaturas)
    print(f"\nEl promedio de la temperatura de la semana es: {promedio_temperaturas} °C.")

    temperaturas_cadena = ', '.join(map(str, temperaturas))
    print(f"\nTodas las temperaturas como cadena separadas por comas: {temperaturas_cadena}")

    dias_calurosos = 0
    for grados in temperaturas:
        if grados >= 24:
            dias_calurosos += 1
    print(f"\nCantidad de días con temperatura igual o superior a 24 °C: {dias_calurosos}")

    temperatura_minima = min(temperaturas)
    temperatura_maxima = max(temperaturas)
    print(f"\nLa temperatura más baja fue: {temperatura_minima} °C")
    print(f"La temperatura más alta fue: {temperatura_maxima} °C")

    temperaturas.clear()
    print("\nLista de temperaturas se ha vaciado:", temperaturas)

    
temperatura_diaria_usuario()
        
        
