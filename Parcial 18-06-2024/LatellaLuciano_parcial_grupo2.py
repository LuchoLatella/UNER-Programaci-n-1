

def temperatura_diaria_usuario():
    temperaturas = []
    for dia in range(1,8):
        temperatura = float(input(f"Por favor ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)

    temperatura_ordenada = sorted(temperaturas)
    print(f"Las temperaturas ordenadas son: {temperatura_ordenada}")



    
temperatura_diaria_usuario = (input("Por favor ingrese un número, para finalizar presione - fin -: "))
        
        
