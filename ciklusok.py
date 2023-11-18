import random


def szamjegyek_osszege():
    szam = random.randint(1, 1000000000)
    szamjegy_osszeg = 0
    for i in range(len(str(szam))):
        szamjegy_osszeg += int(str(szam)[i])

    szamjegyek = [szamjegy_osszeg]

    i = 0
    while not (len(str(szamjegyek[i])) == 1):
        uj_osszeg = 0
        for j in range(len(str(szamjegyek[i]))):
            uj_osszeg += int(str(szamjegyek[i])[j])
        szamjegyek.append(uj_osszeg)
        i += 1

    print(f"Kisorsolt szám: {szam}\n"
          f"{szamjegyek}")
