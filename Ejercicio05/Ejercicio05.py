"""
Realiza un programa que reciba por teclado una 
cantidad de minutos y muestre por pantalla 
a cuantas horas y minutos corresponde.
"""

minutosTotales = int(input("Ingrese una cantidad de minutos: "))

horas = minutosTotales // 60
minutosRestantes = minutosTotales % 60

print(f"Los {minutosTotales} minutos corresponden a {horas} horas y {minutosRestantes} minutos")
