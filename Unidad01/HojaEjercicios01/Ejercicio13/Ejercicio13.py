"""
Un ciclista parte de una ciudad A a
las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra 
ciudad B es de T segundos. Escribir un 
algoritmo que determine la hora de 
llegada a la ciudad B
"""
import sys

print("Ingrese la hora de partida:\n")

horas = int(input("\tHora (0-23): "))
minutos = int(input("\tMinutos (0-59): "))
segundos = int(input("\tSegundos (0-59): "))

while (horas < 0 or horas > 23) or (minutos < 0 or minutos > 59) or (segundos < 0 or segundos > 59):
    print("\nLa hora de salida debe de coincidir con el formato.\n", file = sys.stderr)
    
    print("Ingrese la hora de partida:\n")

    horas = int(input("\tHora (0-23): "))
    minutos = int(input("\tMinutos (0-59): "))
    segundos = int(input("\tSegundos (0-59): "))

tiempoViaje = int(input("\nIngrese el tiempo de viaje de una ciudad a otra en segundos: "))

while tiempoViaje <= 0:
    print("\nEl tiempo del viaje no puede ser igual o inferior a 0.\n", file = sys.stderr)
    
    tiempoViaje = int(input("\nIngrese el tiempo de viaje de una ciudad a otra en segundos: "))

# Partimos de la hora de llegada en segundos
horaInicial = horas * 3600 + minutos * 60 + segundos
horaFinal = horaInicial + tiempoViaje

horasLlegada = (horaFinal // 3600) % 24
minutosLlegada = (horaFinal % 3600) // 60
segundosLlegada = horaFinal % 60

print(f"\nLa hora de llegada ha sido a las {horasLlegada:02d}:{minutosLlegada:02d}:{segundosLlegada:02d}")
