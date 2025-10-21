"""
Escribe un programa que pida el límite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que
introduzcamos el 0.

Cuando termine el programa dará las siguientes informaciones:

- La suma de los números que están dentro del intervalo (intervalo abierto).
- Cuántos números están fuera del intervalo.
- Informa si hemos introducido algún número igual a los límites del intervalo.
"""
def solicitar_numeros():
    try:
        inferior = int(input("\nIngrese el límite inferior: "))
        superior = int(input("Ingrese el límite superior: "))
    except ValueError:
        print("\tIngrese únicamente números enteros")

    if inferior < superior:
        return inferior, superior
    else:
        return solicitar_numeros()


def analizar():
    inferior, superior = solicitar_numeros()

    suma = 0
    contador = 0
    limite_tocado = False
    terminado = False

    print("\n AVISO\n En caso de querer salir del programa, ingresar el '0'\n")

    while not terminado:

        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("\tIngrese únicamente números enteros")
            continue

        if numero == 0:
            terminado = True
        
        if inferior < numero < superior:
            suma += numero
        elif numero == inferior or numero == superior:
            limite_tocado = True
            contador += 1
        else:
            contador += 1
    
    print("\n==============================")
    print("         RESULTADOS           ")
    print("==============================")
    print(f"Suma de los números internos: {suma}")
    print(f"Cantidad de números externos: {contador}")
    print(f"¿Se ha tocado el límite?: {limite_tocado}")
    print("==============================")

# Llamamos al método
analizar()