from funktionen import *

q = 0
zaehler = 1
while True:
    d = float(input("Dicke der " + str(zaehler) + ". Deckenschicht: "))
    m = input("Material der " + str(zaehler) + ". Schicht: ")
    if zaehler == 1:
        n = input("Gebäudenutzung: ")
    else:
        n = "Keine"
    q += deckenlast(d, m, n)
    zaehler += 1
    s = input("Noch eine Deckenschicht? (ja/nein)")
    if s != "ja":
        break

print(q)

tw = input("Tragwerk: ").lower()
adt = input("Einfeld- oder Durchlaufträger?:").lower()
mat = input("Material:").lower()
l = float(input("Länge eines Balkens:"))

if tw == "balken":
    if adt == "einfeldtraeger":
        m = balken_einfeldtraeger(q, l)
    else:
        m = balken_durchlauftraeger(q, l)
    if mat == "holz":
        print("Höhe: " + str(balken_holz_hoehe_breite(m)[0]) + " cm\n"
              + "Breite: " + str(balken_holz_hoehe_breite(m)[1]) + " cm")
    if mat == "stahlbeton_rechteckquerschnitt":
        print("Höhe: " + str(balken_stahlbeton_rechteckquerschnitt_hoehe_breite(m)[0]) + " cm\n"
              + "Breite: " + str(balken_stahlbeton_rechteckquerschnitt_hoehe_breite(m)[1]) + " cm")
    if mat == "stahlbeton_plattenbalken":
        print("Höhe: " + str(balken_stahlbeton_plattenbalken_hoehe_breite(m)[0]) + " cm\n"
              + "Breite: " + str(balken_stahlbeton_plattenbalken_hoehe_breite(m)[1]) + " cm")
    if mat == "stahl":
        print("Höhe: " + str(balken_stahl_hoehe_breite(m)[0]) + " cm\n"
              + "Breite: " + str(balken_stahl_hoehe_breite(m)[1]) + "cm")

if tw == "balkenrost" and mat == "stahlbeton":
    ("Höhe: " + str(balkenrost_stahlbeton_hoehe_breite(m)[0]) + " cm\n"
     + "Breite: " + str(balkenrost_stahlbeton_hoehe_breite(m)[1]) + " cm")

if tw == "platte":
    if adt == "einfeldtraeger":
        li = platte_einfeldtraeger(l)
    if adt == "kragarm":
        li = platte_kragarm(l)
    if adt == "durchlauftraeger_endfeld":
        li = platte_durchlauftraeger_endfeld(l)
    if adt == "durchlauftraeger_innenfeld":
        li = platte_durchlauftraeger_innenfeld(l)
    if li > 4.3:
        print("Höhe der Deckenplatte: " +
              str(platte_stahlbeton_hoehe_b(li)) + " cm")
    else:
        print("Höhe der Deckenplatte: " +
              str(platte_stahlbeton_hoehe_a(li)) + " cm")

if tw == "fachwerk" and adt == "einfeldtraeger" and mat == "stahl":
    print("Höhe der Träger: " + fachwerk_einfeldtraeger_stahl_hoehe)
