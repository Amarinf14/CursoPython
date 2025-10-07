"""
Escribe un programa que lea un
número e indique si es par o impar.
"""

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print(f"El {num} es par")
else:
    print(f"El {num} es impar")
