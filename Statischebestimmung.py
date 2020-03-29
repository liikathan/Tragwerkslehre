a = int(input("Anzahl der verschieblichen Auflager: "))
b = int(input("Anzahlt der unverschieblichen Auflager: "))
c = int(input("Anzahlt der Einspanungen: "))
d = int(input("Anzahl der Gelenke: "))

e = a + 2 * b + 3 * c - 3 - d

if e == 0:
    print("statisch bestimmt")
if e >= 1:
    print("statisch unbestimmt")
if e <= -1:
    print("statisch unterbestimmt")
