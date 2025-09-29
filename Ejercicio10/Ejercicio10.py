"""
Dado un número de dos cifras, diseñe un
algoritmo que permita obtener el número invertido.
"""

numero = input("Ingrese un número de dos cifras: ")

while len(numero) != 2 or not numero.isdigit():
    numero = input("Por favor, ingrese un número de dos cifras: ")

numeroInvertido = numero[::-1]

print(f"El número invertido es: {numeroInvertido}")
