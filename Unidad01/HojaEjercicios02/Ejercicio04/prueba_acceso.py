"""
Algoritmo que pida dos números 'nota' y 'edad'
y un carácter 'sexo' y muestre el mensaje
'ACEPTADA' si la nota es mayor o igual a cinco,
la edad es mayor o igual a dieciocho y el sexo es 'F'.
En caso de que se cumpla lo mismo, pero el sexo sea 'M',
debe imprimir 'POSIBLE'. Si no se cumplen
dichas condiciones se debe mostrar 'NO ACEPTADA
"""

from enum import Enum

class Sexo(Enum):
    F = "F"
    M = "M"

nota = float(input("Ingrese su nota: "))
edad = int(input("Ingrese su edad: "))
sexo_input = input("Ingrese su sexo (F/M): ").upper()

try:
    sexo = Sexo(sexo_input)
except ValueError:
    print("El sexo debe ser 'F o 'M'")
    exit()

if (nota >= 5 and edad >= 18 and sexo == Sexo.F):
    print("ACEPTADA")
elif (nota >= 5 and edad >= 18 and sexo == Sexo.M):
    print("POSIBLE")
else:
    print("NO ACEPTADA")
