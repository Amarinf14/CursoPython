"""
Escribe una función promedio(lista) que
reciba una lista de números y retorne su media
"""
def promedio(numeros: list[int | float]) -> float:
    """
    Calcula el promedio de una lista de números.
    
    Parámetros:
    numeros (list[int | float]): Lista de números.
    
    Retorna:
    float: El promedio de los números en la lista, redondeado a dos decimales.
    
    Raises:
    ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return round(sum(numeros) / len(numeros), 2)

# Ejemplo de uso
mi_lista: list[int | float] = [4.3, 8, 15.8, 16.6, 23, 42]
print(promedio(mi_lista)) # Salida: 18.28
