import piskvorky
import pytest

def test_rozdeleni_symbolu():
    assert piskvorky.rozdeleni_symbolu("x") == "o"
    assert piskvorky.rozdeleni_symbolu("o") == "x"
    with pytest.raises(Exception):
        assert piskvorky.rozdeleni_symbolu("p")

def test_tah_hrace():
    assert piskvorky.tah_hrace("----------", "x", 5) == "----x-----"

def test_vyhodnot():
    with pytest.raises(Exception) as ex1:
        piskvorky.vyhodnot("------xxx-----------")
        assert str(ex1) == "Vyhrály křížky!"
    with pytest.raises(Exception) as ex2:
        piskvorky.vyhodnot("------ooo-----------")
        assert str(ex2) == "Vyhrály kolečka!"
    with pytest.raises(Exception) as ex3:
        piskvorky.vyhodnot("xoxoxoxoxoxo")
        assert str(ex3) == "Remíza!"
    assert piskvorky.vyhodnot("-xoxoxoxo") == "-"

    