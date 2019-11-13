from random import randrange

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

def tah(pole, cislo_policka, symbol):
    # zapíše tah hráče či počítače na dané políčko v poli
    pole = pole[:cislo_policka - 1] + symbol + pole[cislo_policka + 0:]
    return pole

def tah_hrace(pole, symbol):
    # zeptá se na jaké políčko chce hráč umístit svůj symbol, pokud je pole volné, zavolá funkci tah, která tak provede, nakonec vykreslí změněné pole
    cislo_policka = int(input("Jsi na tahu! Zvol políčko 1-20: "))
    while "-" not in pole[cislo_policka - 1]:
        cislo_policka = int(input("Políčko je obsazené. Hraj na volné políčko: "))
    pole = tah(pole, cislo_policka, symbol)
    print (pole)
    return pole
 
def tah_pocitace(pole, pocitac_symbol, symbol):
    # náhodně zvolí pole 1-20, pokud je pole volné, provede tah a vykreslí změněné pole
    print ("Hraje počítač.")
    vole_misto = "-"
    tri_prasatka = pocitac_symbol + pocitac_symbol + vole_misto
    # počítač má dva své symboly vedle sebe, následuje volné místo
    tri_prasatka_nadruhou = vole_misto + pocitac_symbol + pocitac_symbol
    # je volné místo, pak následují dva počítačovo symboly
    tri_selatka = symbol + symbol + vole_misto
    # hráč má dva své symboly vedle sebe, následuje volné místo
    tri_selatka_nadruhou = vole_misto + symbol + symbol
    # je volné místo, následují dva hráčovo symboly
    divocak = pocitac_symbol + vole_misto
    # vedle počítačova symbolu je volné místo zprava
    druhy_divocak = vole_misto + pocitac_symbol
    # vedle počítačova symbolu je volné místo zleva
    # nejprve program zkontroluje, jestli má počítač dva symboly vedle sebe s volným místem vedle, pak zaplní třetí místo svým symbolem
    if tri_prasatka in pole:
        pole = pole.replace(tri_prasatka, pocitac_symbol * 3)
    elif tri_prasatka_nadruhou in pole:
        pole = pole.replace(tri_prasatka_nadruhou, pocitac_symbol * 3)
    # pak zkontroluju, jestli hráč má dva symboly vedle sebe s volným místem, pak počítač zabere volné místo svým symbolem
    elif tri_selatka in pole:
        cast_pole = tri_selatka.replace(vole_misto, pocitac_symbol)
        # volné místo vedle hráčových dvou symbolů nahradí počítač svým symbolem
        pole = pole.replace(tri_selatka, cast_pole)
    elif tri_selatka_nadruhou in pole:
        cast_pole_nadruhou = tri_selatka_nadruhou.replace(vole_misto, pocitac_symbol)
        pole = pole.replace(tri_selatka_nadruhou, cast_pole_nadruhou)
    # pokud nikdo nemá vedle sebe dva symboly, zkontroluje, jestli má počítač jeden symbol v poli s volným místem vedle a obsadí ho svým symbolem
    elif divocak in pole:
        pole = pole.replace(divocak, pocitac_symbol * 2)
    elif druhy_divocak in pole:
        pole = pole.replace(druhy_divocak, pocitac_symbol * 2)
    # pokud žádná z těchto podmínek nenastane, počítač zvolí pole náhodně
    else:
        cislo_policka = randrange (1, 19)
        while "-" not in pole[cislo_policka - 1]:
            cislo_policka = randrange (1, 19)
        pole = tah(pole, cislo_policka, pocitac_symbol)
        print("Počítač hrál pole", cislo_policka)
    print (pole)
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
    vysledek = vyhodnot (pole)
    while vysledek == "-":
        pole = tah_hrace(pole, symbol)
        try: 
            vysledek = vyhodnot (pole)
        except Exception as ex:
            print(str(ex))
            break
        pole = tah_pocitace (pole, pocitac_symbol, symbol)
        try:
            vysledek = vyhodnot (pole)
        except Exception as ex:
            print(str(ex))
            break

piskvorky1d()