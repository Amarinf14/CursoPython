"""
Pedir el nombre y los dos apellidos de
una persona y mostrar las iniciales.
"""

name = str(input("Ingrese su nombre: "))
surname1 = str(input("Ingrese su primer apellido: "))
surname2 = str(input("Ingrese su segundo apellido: "))

# Usar upper() o lower() en caso de que sea necesario
initials = name[0] + surname1[0] + surname2[0]

print(f'\nSus iniciales: {initials}')
