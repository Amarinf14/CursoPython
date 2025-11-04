"""
Añade docstring explicativos a las funciones anteriores.
Usa `help(funcion)` o `funcion.__doc__` para comprobarlos
"""

# Ejercicio 1
def saludar(nombre: str) -> str:
    """
    Devuelve un saludo personalizado para el nombre dado.
    
    Parámetros:
    nombre (str): El nombre de la persona a saludar.
    
    Retorna:
    str: Mensaje de saludo con la inclusión del nombre.
    """
    return f"Hola, {nombre}!"

print(saludar("Marín"))

# Ejercicio 2
def suma(a: float, b:float) -> float:
    """
    Devuelve la suma de dos números.
    
    Parámetros:
    a (float): El primer número.
    b (float): El segundo número.
    
    Retorna:
    float: La suma de a y b.
    """
    return a + b

print(suma(3, 5))
print(suma(3.5, 2.7))

# Ejercicio 3
import math

def area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetros:
    radio (float): El radio del círculo.
    
    Retorna:
    float: El área del círculo, redondeada a dos decimales.
    """
    return round(math.pi * (radio ** 2), 2)

print(area_circulo(5))
print(area_circulo(10))

# Ejercicio 4
contador: int = 0

def incrementar():
    """
    Incrementa el valor de la variable global contador en 1.
    """
    global contador
    contador += 1

for _ in range(5):
    print(f'Contador antes de incrementar: {contador}')
    incrementar()
    print(f'Contador después de incrementar: {contador}\n')

def incrementar_sin_global():
    """
    Incrementa una variable local contador en 1 e imprime su valor.
    Esta función no afecta a la variable global contador.
    """
    contador = 0
    contador += 1
    print(f'Contador dentro de incrementar_sin_global: {contador}')

incrementar_sin_global()
print(f"Después de llamar a incrementar_sin_global: {contador}")

# Nota: A partir de aquí, se emepezarán a usar docstrings en los ejercicios.

# Comprobación de docstrings mediante help() y __doc__
help(saludar)
print(suma.__doc__)
