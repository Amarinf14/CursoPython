"""
Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de
un triángulo. El programa debe determinar qué tipo
de triángulo es, teniendo en cuenta lo siguiente:

- Si se cumple Pitágoras entonces es triángulo rectángulo
- Si sólo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno
"""

a = float(input("Introduce el lado A: "))
b = float(input("Introduce el lado B: "))
c = float(input("Introduce el lado C: "))

if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("Triángulo rectángulo")
elif a == b == c:
    print("Triángulo equilátero")
elif a == b or a == c or b == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
