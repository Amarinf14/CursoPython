"""
Dados dos números, mostrar la suma,
resta, división y multiplicación de ambos
"""

numero1 = 5
numero2 = 2

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")

if numero2 != 0:
    division = numero1 / numero2
    print(f"División: {division:.2f}")
else:
    print("División: No se puede dividir entre 0")
