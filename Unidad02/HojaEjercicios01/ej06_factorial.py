"""
Función factorialque calcule el factorial de un número 
entero que no sea negativo. 
Lanzar error si el número no es entero o bien es negativo
"""
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.
    
    Parámetros:
    n (int): Número entero no negativo del cual se desea calcular el factorial.
    
    Retorna:
    int: El factorial de n.
    
    Raises:
    ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número no debe ser negativo.")
    if n == 0:
        return 1
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        
    return resultado

print(factorial(5))  # Salida: 120
print(factorial(0))  # Salida: 1
# print(factorial(-3))  # Lanza ValueError
