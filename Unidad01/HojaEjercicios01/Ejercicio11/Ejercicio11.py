"""
Dadas dos variables numéricas A y B, que el usuario
debe teclear, se pide realizar un algoritmo que
intercambie los valores de ambas variables y 
muestre cuanto valen al final las dos variables.
"""

a = input("Ingrese el valor de la variable A: ")
b = input("Ingrese el valor de la variable B: ")

a, b = b, a

print(f"Ahora la variable A es {a} y la variable B es {b}")
