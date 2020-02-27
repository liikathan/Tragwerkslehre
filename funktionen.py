import os
import math
from xml.etree import ElementTree as ET


def deckenlast(mdicke, baustoff, nutzlast="Keine"):
    file = ET.parse("Tabellenwerte.xml").getroot()

    for tag in file.findall("Baustoffe/" + baustoff):
        value = tag.find("Volumen")
        baustoff = float(value.text)

    for tag in file.findall("Nutzlasten"):
        value = tag.find(nutzlast)
        nutzlast = float(value.text)

    return float(mdicke * baustoff + nutzlast)


def balken_einfeldtraeger(q, l):
    m = q * l * l / 8
    return m


def balken_durchlauftraeger(q, l):
    m = q * l * l / 10
    return m


def balken_holz_hoehe_breite(m):
    h = 6.5 * m**0.5
    b = 0.7 * h
    return [h, b]


def balken_stahlbeton_rechteckquerschnitt_hoehe_breite(m):
    h = 3.2 * math.sqrt(m) + 5
    b = 0.6 * h
    return [h, b]


def balken_stahlbeton_plattenbalken_hoehe_breite(m):
    h = 1.9 * m ** 0.5 + 5
    b = 0.6 * h
    return [h, b]


def balken_stahl_hoehe_breite(m):
    h = b = (360 * m)**(1/3) - 2
    return [h, b]


def balkenrost_stahlbeton_hoehe_breite(l):
    h = l / 20
    b = 0.6 * h
    return [h, b]


def platte_einfeldtraeger(l):
    li = l
    return li


def platte_kragarm(l):
    li = 2.4 * l
    return li


def platte_durchlauftraeger_endfeld(l):
    li = 0.8 * l
    return li


def platte_durchlauftraeger_innenfeld(l):
    li = 0.6 * l
    return li


def platte_stahlbeton_hoehe_a(li):
    h = li / 35 + 0.02
    return h


def platte_stahlbeton_hoehe_b(li):
    h = li * li / 150 + 0.02
    return h


def fachwerk_einfeldtraeger_stahl_hoehe(l):
    h = l / 15
    return h
