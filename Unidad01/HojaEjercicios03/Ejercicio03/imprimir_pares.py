"""
Escribir un programa que imprima todos los números
pares entre dos números que se le pidan al usuario
"""

# 1. Solicitamos los números al usuario
try:
    inicio = int(input("Ingrese el primer número: "))
    fin = int(input("Ingrese el segundo numero número: "))
except ValueError:
    print("Ingrese únicamente números enteros")
    exit()

# 2. Nos aseguramos que el bucle 'for' siempre vaya del menor al mayor
num_menor = min(inicio, fin)
num_mayor = max(inicio, fin)

# 3. Imprimimos los números pares
print(f"Números pares entre {num_menor} y {num_mayor}:")

for numero in range (num_menor, num_mayor + 1):
    if (numero % 2) == 0:
        print(numero)
