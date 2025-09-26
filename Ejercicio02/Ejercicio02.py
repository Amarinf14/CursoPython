"""
Calcular el perímetro y área de un 
rectángulo dada su base y su altura.
"""

base = 5
altura = 3

def medidas(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area

perimetro, area = medidas(base, altura)

print(f"Perímetro: {perimetro}, Área: {area}")
