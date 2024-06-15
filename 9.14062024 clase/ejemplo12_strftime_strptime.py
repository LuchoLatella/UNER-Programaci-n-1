from datetime import datetime
import locale
import prog1

prog1.titulo("datetime.strftime()")

fecha_hora_actual = datetime.now()
print("fecha_hora_actual:", fecha_hora_actual)
print("datetime.strftime():", datetime.strftime(fecha_hora_actual, "%d/%M/%Y"))
print("datetime.strftime():", datetime.strftime(fecha_hora_actual, "%d/%m/%Y %H:%M:%S"))
print("Día:", datetime.strftime(fecha_hora_actual, "%A"))
print("Mes:", datetime.strftime(fecha_hora_actual, "%B"))

locale.setlocale(locale.LC_ALL, 'es_AR.utf8')

print("Día:", datetime.strftime(fecha_hora_actual, "%A"))
print("Mes:", datetime.strftime(fecha_hora_actual, "%B"))

prog1.titulo("datetime.strptime()")

inicio_curso_str = '20/03/2022'
inicio_curso_date = datetime.strptime(inicio_curso_str, '%d/%m/%Y')
print("Año:", inicio_curso_date.year)
print("Mes:", inicio_curso_date.month)
print("Día:", inicio_curso_date.day)
