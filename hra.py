import piskvorky

try:
    delka_pole = piskvorky.ai.delka_pole()
    piskvorky.piskvorky1d(delka_pole)
except Exception as ex:
    print(str(ex))