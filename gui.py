from tkinter import *
from funktionen import *

window = Tk()
window.title("Deckenlast")
window.geometry("600x600")

q = 0
zaehler = 1
while True:
    d = Label(window, text=float(
        input("Dicke der " + str(zaehler) + ". Deckenschicht: ")))
    d.pack()
    m = Label(window, text=input(
        "Material der " + str(zaehler) + ". Schicht: "))
    m.pack()
    if zaehler == 1:
        n = Label(window, text=input("Gebäudenutzung: "))
    else:
        n = "Keine"
    q += deckenlast(d, m, n)
    zaehler += 1
    s = input("Noch eine Deckenschicht? (ja/nein)")
    if s != "ja":
        break

Ergebnis = Label(window, text=q,)

window.mainloop()
