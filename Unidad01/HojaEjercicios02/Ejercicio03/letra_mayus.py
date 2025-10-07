"""
Programa que lea una cadena por teclado
y compruebe si es una letra mayúscula.
"""

letra = input("Ingrese una letra: ")

if (len(letra) == 1 and letra.isalpha()):
    if (letra.isupper()):
        print(f"La '{letra}' es mayúscula")
    else:
        print(f"La '{letra}' es minúscula")
else:
    print("Debe ingresar una letra")
