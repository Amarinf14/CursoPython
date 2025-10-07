"""
Escribir un algoritmo para calcular la nota final
de un estudiante, considerando que por cada respuesta
correcta 5 puntos, por una incorrecta -1 y por respuestas
en blanco 0. Imprime el resultado obtenido por el estudiante.
"""

correctas = int(input("Ingrese el número de respuestas correctas: "))
incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
blanco = int(input("Ingrese el número de respuestas en blanco: "))

puntos_totales = (correctas + incorrectas + blanco) * 5
nota_final = (correctas * 5) + (incorrectas * (-1))

print(f'La nota final es: {nota_final} sobre {puntos_totales}')
