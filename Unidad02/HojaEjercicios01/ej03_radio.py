"""
Crea una función area_circulo(radio)que
devuelva el area de un círculo usando pi. 
Debes utilizar la clase math e importar el 
módulo y usar la función match.pi.
"""
import math

def area_circulo(radio: float) -> float:
    return round(math.pi * (radio ** 2), 2)

# Ejemplo de uso
print(area_circulo(5)) # Salida: 78.54
print(area_circulo(10)) # Salida: 314.16
