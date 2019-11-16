import ai

def test_tah_pocitace():
    assert ai.tah_pocitace("---xx---------------", "x", "o") == "---xxx--------------"
    assert ai.tah_pocitace("---xxo--------------", "x", "o") == "--xxxo--------------"
    assert ai.tah_pocitace("---oo---------------", "x", "o") == "---oox--------------"
    assert ai.tah_pocitace("---oox--------------", "x", "o") == "--xoox--------------"
    assert ai.tah_pocitace("---x----------------", "x", "o") == "---xx---------------"
    assert ai.tah_pocitace("---xo---------------", "x", "o") == "--xxo---------------"
    pole = ai.tah_pocitace("-"*20, "x", "o")
    assert len(pole) == 20
    assert pole.count("x") == 1
    assert pole.count("-") == 19