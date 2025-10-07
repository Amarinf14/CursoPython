"""
La política de cobro de una compañía telefónica es:
cuando se realiza una llamada, el cobro es por el
tiempo que ésta dura, de tal forma que:

- los primeros cinco minutos cuestan 1 euro
- los siguientes tres, 80 céntimos
- los siguientes dos minutos, 70 céntimos
- y a partir del décimo minuto, 50 céntimos. Además, 
se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de
tarde, 10 %. 

Realice un algoritmo para determinar cuánto debe pagar
por cada concepto una persona que realiza una llamada.
"""

duracion = float(input("Ingrese la duración de la llamada en minutos: "))
dia = input("Ingrese el día de la llamada (domingo/otro): ").lower()

if duracion <= 5:
    costo = 1.0
elif duracion <= 8:
    costo = 1.0 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo = 1.0 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo = 1.0 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

impuesto = 0

if dia == "domingo":
    impuesto = 0.03
elif dia == "otro":
    turno = input("Turno (mañana/tarde): ").lower()
    if turno == "mañana":
        impuesto = 0.15
    elif turno == "tarde":
        impuesto = 0.10
    else:
        print("Indique mañana o tarde.")
else:
    print("Indique domingo u otro.")

total = costo + costo * impuesto

print(f"Costo base: {costo:.2f} €")
print(f"Total a pagar: {total:.2f} €")
