# Este programa recibe como argumentos desde la terminal o consola de comandos
# el parámetro operacion y dos operandos (operando1 y operando2) y ejecuta la operación matemática.

import sys

operacion = sys.argv[1]
operando1 = int(sys.argv[2])
operando2 = int(sys.argv[3])

match operacion:
    case "sumar":
        str_operacion = str(operando1) + " + " + str(operando2) + " = "
        res = operando1 + operando2
    case "restar":
        str_operacion = str(operando1) + " - " + str(operando2) + " =" 
        res = operando1 - operando2
    case "multiplicar":
        str_operacion = str(operando1) + " * " + str(operando2) + " = "
        res = operando1 * operando2
    case "dividir":
        str_operacion = str(operando1) + " / " + str(operando2) + " = "
        res = operando1 / operando2
        
print(str_operacion + str(res))
