from datetime import datetime

final_mundial_2018 = datetime(2018, 9, 15)
actual = datetime.now()

diferencia = actual - final_mundial_2018
print(diferencia)
print("Días:", diferencia.days)
print("Segundos:", diferencia.seconds)
