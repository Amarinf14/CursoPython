"""
Un vendedor recibe un sueldo base mas un 10% 
extra por comisión de sus ventas, el vendedor desea 
saber cuanto dinero obtendrá por concepto de comisiones 
por las tres ventas que realiza en el mes y el total que 
recibirá en el mes tomando en cuenta su sueldo base y comisiones
"""
from typing import List

sueldoBase = float(input("Ingrese su sueldo base: "))
numVentas: int = 3

ventas: List[float] = [] # Hacemos que Pylance haga la inferencia correctamente
for i in range(1, numVentas + 1):
    venta = float(input(f"Ingrese el monto de la venta {i}: "))
    ventas.append(venta)

percepcionComision = sum(venta * 0.10 for venta in ventas)  # 10% de cada venta
sueldoTotal = sueldoBase + percepcionComision

print(f"-> Percepción por comisiones: {percepcionComision}")
print(f"-> El sueldo total es: {sueldoTotal}")
