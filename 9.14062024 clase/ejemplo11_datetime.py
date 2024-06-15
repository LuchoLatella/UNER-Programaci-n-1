import datetime
import prog1

prog1.titulo("datetime")

fecha_hora = datetime.datetime(1985, 10, 26)
print("fecha_hora:", fecha_hora)
print("Año:", fecha_hora.year)
print("Mes:", fecha_hora.month)
print("Día:", fecha_hora.day)
print("________________________")
print("Año:", getattr(fecha_hora, 'year'))
print("Mes:", getattr(fecha_hora, 'month'))
print("Día:", getattr(fecha_hora, 'day'))

prog1.titulo("datetime.datetime.now()")

fecha_hora_actual = datetime.datetime.now()
print("fecha_hora_actual:", fecha_hora_actual)
print("Año:", fecha_hora_actual.year)
print("Mes:", fecha_hora_actual.month)
print("Día:", fecha_hora_actual.day)