"""
Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar
es mayor o menor que el introducido, además de los intentos que te quedan
(tienes 10 intentos para acertarlo).
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has
acertado), si se llega al límite de intentos te muestra el número que había generado.
"""
import random

def adivinar_numero():
    # 1. Generar el número aleatorio entre 1 y 100 (incluidos)
    numero_secreto = random.randint(1, 100)
    
    # 2. Definir los límites del juego
    MAX_INTENTOS = 10
    intentos_realizados = 0

    print("=========================================")
    print("      ¡Adivina el Número Secreto!       ")
    print("=========================================")

    # Bucle principal del juego
    while intentos_realizados < MAX_INTENTOS:
        
        # 3. Pedir la entrada del usuario
        try:
            intento = int(input(f"\nIntento {intentos_realizados + 1}\nTe quedan {MAX_INTENTOS - intentos_realizados} intentos: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            continue # Vuelve al inicio del bucle sin contar este intento fallido
        
        # Incrementar el contador de intentos
        intentos_realizados += 1

        # 4. Comprobar si se acertó el número
        if intento == numero_secreto:
            print("\nHas adivinado el número!")
            print(f"El número secreto era el {numero_secreto}.")
            print(f"Lo has acertado en {intentos_realizados} intentos.")

            return # Termina la función y el juego

        # 5. Dar pistas al usuario
        elif intento < numero_secreto:
            print("El número a adivinar es mayor que el introducido.")
        elif intento > numero_secreto:
            print("El número a adivinar es menor que el introducido.")
    
    # 6. Fin del juego por límite de intentos
    
    print("\n=========================================")
    print("                Game Over                ")
    print(f"El número secreto era el {numero_secreto}")
    print("=========================================")

# Ejecutar la aplicación
if __name__ == "__main__":
    adivinar_numero()