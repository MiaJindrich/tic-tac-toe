import util

def test_tah():
    pole = "-" * 10
    pole = util.tah(pole, 5, "o")
    assert pole == "----o-----"
    assert len(pole) == 10
    assert pole.count("o") == 1
    assert pole.count("-") == 9
    assert pole[5-1] == "o"