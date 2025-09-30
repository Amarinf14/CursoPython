"""
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se
compone de los siguientes porcentajes:
    - 55% del promedio de sus tres calificaciones parciales.
    - 30% de la calificación del examen final.
    - 15% de la calificación de un trabajo final
"""

examen1 = float(input("Ingrese la nota del primer examen: "))
examen2 = float(input("Ingrese la nota del segundo examen: "))
examen3 = float(input("Ingrese la nota del tercer examen: "))

mediaExmanes = (examen1 + examen2 + examen3) / 3

examenFinal = float(input("Ingrese la nota del examen final: "))
trabajoFinal = float(input("Ingrese la nota del trabajo final: "))

calificacionFinal = (mediaExmanes * 0.55) + (examenFinal * 0.3)+ (trabajoFinal * 0.15)

print(f"Su calificación final es {calificacionFinal:.2f}")
