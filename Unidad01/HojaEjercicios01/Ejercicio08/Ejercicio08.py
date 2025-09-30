"""
Pide al usuario dos números y muestra la "distancia" 
entre ellos (el valor absoluto de su diferencia, de
modo que el resultado sea siempre positivo).
"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

distancia = abs(numero1 - numero2)

print(f"la distancia entre ambos números es de {distancia} metros")
