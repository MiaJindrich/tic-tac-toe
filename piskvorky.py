from random import randrange

def vyhodnot(pole):
    if "x" * 3 in pole:
        vysledek = "Vyhrály křížky!"
    elif "o" * 3 in pole:
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
 
def tah_pocitace(pole, pocitac_symbol, symbol):
    print ("Hraje počítač.")
    vole_misto = "-"
    tri_prasatka = pocitac_symbol + pocitac_symbol + vole_misto
    tri_prasatka_nadruhou = vole_misto + pocitac_symbol + pocitac_symbol
    tri_selatka = symbol + symbol + vole_misto
    tri_selatka_natruhou = vole_misto + symbol + symbol
    # zkontroluju, jestli počítač má dva symboly vedle sebe
    if tri_prasatka in pole:
        pole = pole.replace(tri_prasatka, pocitac_symbol * 3)
    elif tri_prasatka_nadruhou in pole:
        pole = pole.replace(tri_prasatka_nadruhou, pocitac_symbol * 3)
    # pak zkontroluju, jestli hráč nemá dva symboly vedle sebe
    elif tri_selatka in pole:
        cast_pole = tri_selatka.replace(vole_misto, pocitac_symbol)
        pole = pole.replace(tri_selatka, cast_pole)
    elif tri_selatka_natruhou in pole:
        cast_pole_nadruhou = tri_selatka_natruhou.replace(vole_misto, pocitac_symbol)
        pole = pole.replace(tri_selatka_natruhou, cast_pole_nadruhou)
    else:
        cislo_policka = randrange (20)
        while "-" not in pole[cislo_policka - 1]:
            cislo_policka = randrange (20)
        pole = tah(pole, cislo_policka, pocitac_symbol)
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
        pole = tah_pocitace (pole, pocitac_symbol, symbol)
        vysledek = vyhodnot (pole)
    print (vyhodnot(pole))

print("Hrací pole: --------------------")
piskvorky1d()