import os
from xml.etree import ElementTree as ET


def Last(eigenlast, nutzlast):

    def eigenlast(schichten, deckenbelag):
        schichten = int(input("Anzahl der Schichten: "))

        def deckenbelag(baustoff, mdicke):
            file = ET.parse("Tabellenwerte.xml").getroot()

            for tag in file.findall("Baustoffe/" + baustoff):
                value = tag.find("Volumen")
                baustoff = float(value.text)
                baustoff = int(baustoff * 100)
            mdicke = int(mdicke * 100)

            return (baustoff * mdicke * 0.0001)
        for i in range(schichten):
            return(deckenbelag())
            i = i + deckenbelag()

    def nutzlast(Nutzung):
        file = ET.parse("Tabellenwerte.xml").getroot()

        for tag in file.findall("Nutzlasten/" + Nutzung):
            value = tag.find("Vorgabewert")
            value = float(value.text)

        return value

    return (eigenlast + nutzlast)
