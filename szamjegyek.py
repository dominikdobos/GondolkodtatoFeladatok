def szamjegy_int():
    szam = int(input("3 jegyű szám: "))
    while not (99 < szam < 1000):
        szam = int(input("Hiba! 3 jegyű szám: "))

    egyes = szam % 10
    tizes = ((szam % 100) - egyes) // 10
    szazas = (szam - (tizes + egyes)) // 100
    print(f"{szazas} {tizes} {egyes}")


def szamjegy_string():
    szam = int(input("3 jegyű szám: "))
    while not (99 < szam < 1000):
        szam = int(input("Hiba! 3 jegyű szám: "))

    szamjegyek = []

    for i in range(len(str(szam))):
        szamjegyek.append(str(szam)[i])

    for i in range(len(szamjegyek)):
        print(szamjegyek[i], end=" ")
