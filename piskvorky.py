from random import randrange

def vyhodnot(pole):
    if "xxx" in pole:
        vysledek = "Vyhrály křížky!"
    elif "ooo" in pole:
        vysledek = "Vyhrály kolečka!"
    elif "-" not in pole:
        vysledek = "Remíza!"
    else:
        vysledek = "-"

    return vysledek

def tah(pole, cislo_policka, symbol):
    pole = pole[:cislo_policka - 1] + symbol + pole[cislo_policka + 0:]
    return pole

def tah_hrace(pole, symbol):
    cislo_policka = int(input("Jsi na tahu! Zvol políčko 1-20: "))
    pole = tah(pole, cislo_policka, symbol)
    print (pole)
    return pole
 
def tah_pocitace(pole, pocitac_symbol):
    print ("Hraje počítač.")
    symbol = pocitac_symbol
    cislo_policka = randrange (20)
    while "-" not in pole[cislo_policka]:
        cislo_policka = randrange (20)
    pole = tah(pole, cislo_policka, symbol)
    print (pole)
    return pole

def piskvorky1d():
    pole = "--------------------"
    symbol = input("Jaký symbol hraješ? ")
    if symbol == "o":
        pocitac_symbol = "x"
    else:
        pocitac_symbol = "o"
    vysledek = vyhodnot (pole)
    while vysledek == "-":
        pole = tah_hrace(pole, symbol)
        vysledek = vyhodnot (pole)
        pole = tah_pocitace (pole, pocitac_symbol)
        vysledek = vyhodnot (pole)
    print (vyhodnot(pole))

piskvorky1d()