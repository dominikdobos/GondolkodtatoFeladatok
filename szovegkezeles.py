def hanyszor():  # kis-, nagybetű is számít
    szoveg = input("Kérek egy szöveget: ")
    keresett_szoveg = input("A keresett szöveg: ")
    db = szoveg.count(keresett_szoveg)

    print(f"A szövegben \"{szoveg}\", a(z) \"{keresett_szoveg}\" szöveg {db} darabszor fordul elő.")


def hanyszor_ignoral():  # kis-, nagybetű nem számít
    szoveg = input("Kérek egy szöveget: ")
    keresett_szoveg = input("A keresett szöveg: ")

    kicsi_sz = szoveg.lower()
    kicsi_ksz = keresett_szoveg.lower()
    db = kicsi_sz.count(kicsi_ksz)

    print(f"A szövegben \"{szoveg}\", a(z) \"{keresett_szoveg}\" szöveg {db} darabszor fordul elő.")
