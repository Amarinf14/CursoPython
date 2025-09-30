"""
Pide al usuario dos pares de números x1,y1 y x2,y2,
que representen dos puntos en el plano. Calcula y
muestra la distancia entre ellos.
"""
import math

x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))

x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print(f"La distancia entre los puntos es: {distancia:.2f}")
