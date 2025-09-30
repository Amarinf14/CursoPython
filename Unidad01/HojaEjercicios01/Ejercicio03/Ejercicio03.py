"""
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.Debes utilizar la clase math e
importar el módulo y usar la función match.sqrt(). Ejemplo:

```python
import math

numero = 16
raiz = math.sqrt(numero)
print("La raíz cuadrada de", numero, "es", raiz)
```
"""
import math

cateto1 = 16
cateto2 = 17

hipotenusa = math.sqrt(math.pow(cateto1, 2) + cateto2**2)

print(f"La hipotenusa es: {hipotenusa:.2f}")
