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
    while "-" not in pole[cislo_policka - 1]:
        cislo_policka = int(input("Políčko je obsazené. Hraj na volné políčko: "))
    pole = tah(pole, cislo_policka, symbol)
    print (pole)
    return pole
 
def tah_pocitace(pole, pocitac_symbol):
    print ("Hraje počítač.")
    symbol = pocitac_symbol
    if "xx-" in pole:
        pole = pole.replace("xx-", "xx" + pocitac_symbol)
    elif "-xx" in pole:
        pole = pole.replace("-xx", pocitac_symbol + "xx")
    elif "oo-" in pole:
        pole = pole.replace("oo-", "oo" + pocitac_symbol)
    elif "-oo" in pole:
        pole = pole.replace("-oo", pocitac_symbol + "oo")
    else:
        cislo_policka = randrange (20)
        while "-" not in pole[cislo_policka - 1]:
            cislo_policka = randrange (20)
        pole = tah(pole, cislo_policka, symbol)
        print("Počítač hrál pole", cislo_policka)
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

print("Hrací pole: --------------------")
piskvorky1d()