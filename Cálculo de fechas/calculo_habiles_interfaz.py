import tkinter as tk
from tkinter import ttk
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

def calcular():
    fecha_inicio_str = fecha_inicio_entry.get()
    fecha_fin_str = fecha_fin_entry.get()

    fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
    fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%d-%m-%Y")

    total_dias = (fecha_fin - fecha_inicio).days + 1
    dias_habiles = contar_dias_habiles(fecha_inicio, fecha_fin)
    dias_no_habiles = total_dias - dias_habiles

    resultado_label.config(text=f"Cantidad total de días: {total_dias}\nDías hábiles: {dias_habiles}\nDías no hábiles: {dias_no_habiles}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Días")

# Crear y colocar los widgets en la ventana
fecha_inicio_label = ttk.Label(root, text="Fecha de inicio (DD-MM-AAAA):")
fecha_inicio_label.grid(row=0, column=0, padx=5, pady=5)

fecha_inicio_entry = ttk.Entry(root)
fecha_inicio_entry.grid(row=0, column=1, padx=5, pady=5)

fecha_fin_label = ttk.Label(root, text="Fecha de fin (DD-MM-AAAA):")
fecha_fin_label.grid(row=1, column=0, padx=5, pady=5)

fecha_fin_entry = ttk.Entry(root)
fecha_fin_entry.grid(row=1, column=1, padx=5, pady=5)

calcular_button = ttk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar el bucle de eventos
root.mainloop()