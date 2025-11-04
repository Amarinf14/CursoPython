"""
Variables locales y globales.
- Declara una variable global contador=0
- Escribe una función incrementar() que aumente en 1 el valor de contador
- Imprime contador antes y después de llamar la función. 
(Prueba qué pasa si olvidas usar `global` dentro de la función).
"""
contador: int = 0 # Variable global

def incrementar():
    global contador  # Indica que usaremos la variable global
    contador += 1

for _ in range(5):
    print(f'Contador antes de incrementar: {contador}')
    incrementar()
    print(f'Contador después de incrementar: {contador}\n')

def incrementar_sin_global():
    contador = 0  # Variable local
    contador += 1
    print(f'Contador dentro de incrementar_sin_global: {contador}') # Imprime 1 siempre

incrementar_sin_global()
print(f"Después de llamar a incrementar_sin_global: {contador}") # Imprime 5, no cambia el global
