"""
Crea un programa que pida al usuario dos
números y muestre su división si el segundo
no es cero, o un mensaje de aviso en caso contrario
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num2 != 0:
    print(f"Resultado: {num1/num2: .2f}")
else:
    print("No se puede divir entre 0")
