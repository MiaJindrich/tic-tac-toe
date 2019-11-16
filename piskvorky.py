import ai
import util

def vyhodnot(pole):
    # program vyhodnotí situaci v poli a podle toho buď hra pokračuje, někdo vyhrál, nebo došly volný políčka
    # pokud se hra ukončí, vyhodí to exception, do který uloží výsledek hry
    pocet_symbolu = 3
    if "x" * pocet_symbolu in pole:
        vysledek = "Vyhrály křížky!"
        raise Exception (vysledek)
    elif "o" * pocet_symbolu in pole:
        vysledek = "Vyhrály kolečka!"
        raise Exception (vysledek)
    elif "-" not in pole:
        vysledek = "Remíza!"
        raise Exception (vysledek)
    else:
        vysledek = "-"

    return vysledek

def tah_hrace(pole, symbol, cislo_policka):
    pole = util.tah(pole, cislo_policka, symbol)
    return pole

def rozdeleni_symbolu(symbol):
    if symbol == "o":
        pocitac_symbol = "x"
    elif symbol == "x":
        pocitac_symbol = "o"
    else:
        raise Exception("Zadal jsi symbol špatně.")
        # pokud nedostane x ani o, zachytí chybu a printne zprávu
    return pocitac_symbol

def piskvorky1d():
    # nastaví výchozí pole, zeptá se hráče na symbol, přidělí počítači druhý symbol a vyhodnotí stav pole
    # dokud jsou na poli volná místa, hra pokračuje
    # pokud program vyhodnotí, že jeden z hráčů vyhrál nebo už na poli není volné místo, hra končí
    pole = "-" * 20
    symbol = input("Jaký symbol hraješ? (o/x): ")
    symbol = symbol.lower()
    try:
        # pokusí se spustit funkci rozdeleni_symbolu
        pocitac_symbol = rozdeleni_symbolu(symbol)
    except Exception as ex:
        print(str(ex))
    while symbol != "o" and symbol != "x":
        symbol = input("Zvol si jako symbol o nebo x! ")
        symbol = symbol.lower()
        try:
            pocitac_symbol = rozdeleni_symbolu(symbol)
        except Exception as ex:
            print(str(ex))
    vysledek = vyhodnot(pole)
    while vysledek == "-":
        # zeptá se na jaké políčko chce hráč umístit svůj symbol, pokud je pole volné, zavolá funkci tah, která tak provede, nakonec vykreslí změněné pole
        cislo_policka = int(input("Jsi na tahu! Zvol políčko 1-20: "))
        while "-" not in pole[cislo_policka - 1]:
            cislo_policka = int(input("Políčko je obsazené. Hraj na volné políčko: "))
        pole = tah_hrace(pole, symbol, cislo_policka)
        print(pole)
        try: 
            vysledek = vyhodnot(pole)
        except Exception as ex:
            print(str(ex))
            break
        pole = ai.tah_pocitace(pole, pocitac_symbol, symbol)
        try:
            vysledek = vyhodnot(pole)
        except Exception as ex:
            print(str(ex))
            break

