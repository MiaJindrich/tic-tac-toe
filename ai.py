import random
import util

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
        cislo_policka = random.randrange (1, 19)
        while "-" not in pole[cislo_policka - 1]:
            cislo_policka = random.randrange (1, 19)
        pole = util.tah(pole, cislo_policka, pocitac_symbol)
        print("Počítač hrál pole", cislo_policka)
    return pole