"""
Realizar un algoritmo que pida números (se pedirá por teclado
la cantidad de números a introducir).
El programa debe informar de cuántos números introducidos son
mayores que 0, menores que 0 e iguales a 0.
"""

def clasificar_numeros():
    # Inicializar contadores
    mayores_cero = 0
    menores_cero = 0
    iguales_cero = 0
    
    # --- 1. Pedir la cantidad de números a introducir ---
    while True:
        try:
            cantidad_numeros = int(input("¿Cuántos números deseas introducir? "))
            if cantidad_numeros > 0:
                break
            else:
                print("Por favor, introduce un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

    # --- 2. Procesar la cantidad de números especificada ---
    print(f"\nIntroduce {cantidad_numeros} números:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                # Pedir el número actual
                numero = float(input(f"Número {i + 1}: "))
                
                # Clasificar el número
                if numero > 0:
                    mayores_cero += 1
                elif numero < 0:
                    menores_cero += 1
                else:  # numero == 0
                    iguales_cero += 1
                
                # Salir del bucle interno si la entrada es válida
                break
                
            except ValueError:
                print("Entrada no válida. Introduce un valor numérico.")

    # --- 3. Informar los resultados ---
    print("\n==============================")
    print("         RESULTADOS           ")
    print("==============================")
    print(f"Números mayores que 0: {mayores_cero}")
    print(f"Números menores que 0: {menores_cero}")
    print(f"Números iguales a 0: {iguales_cero}")
    print("==============================")

# Ejecutar el algoritmo
clasificar_numeros()