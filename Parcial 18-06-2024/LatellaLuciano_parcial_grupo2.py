
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



    
temperatura_diaria_usuario()
        
        
