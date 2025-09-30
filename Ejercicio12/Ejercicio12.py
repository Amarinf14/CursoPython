"""
Dos vehículos viajan a diferentes velocidades
(v1 y v2) y están distanciados por una distancia d. 
El que está detrás viaja a una velocidad mayor. 
Se pide hacer un algoritmo para ingresar la distancia 
entre los dos vehículos (km) y sus respectivas velocidades
(km/h) y con esto determinar y mostrar en que tiempo
(minutos) alcanzará el vehículo más rápido al otro.
"""

import sys

v1 = int(input("Ingrese la velocidad del vehículo 1 (km/h): "))
v2 = int(input("Ingrese la velocidad del vehículo 2 (km/h): "))

distancia = int(input("Ingrese la distancia entre los dos vehículos (km): "))

while v1 == v2:
    # Mostramos el mensaje desde la salida de error
    print("Ambos vehículos no pueden mantener la misma velocidad.\n", file = sys.stderr)
    
    v1 = int(input("Ingrese la velocidad del vehículo 1 (km/h): "))
    v2 = int(input("Ingrese la velocidad del vehículo 2 (km/h): "))

while distancia <= 0:
    print("La distancia entre los vehículos debe ser superior a 0", file = sys.stderr)
    
    distancia = int(input("Ingrese la distancia entre los dos vehículos (km): "))


tiempo = (distancia / abs(v1 - v2)) * 60

print(f"Los vehículos tardaran {tiempo:.2f} minutos en encontrase")
