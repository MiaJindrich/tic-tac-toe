def tah(pole, cislo_policka, symbol):
    # zapíše tah hráče či počítače na dané políčko v poli
    pole = pole[:cislo_policka - 1] + symbol + pole[cislo_policka + 0:]
    return pole