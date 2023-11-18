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


def idokezeles():
    ervenyes_idokoz = False

    ido1 = input("1. Kérek egy időt 'óra:perc:mp' formátumban: ")
    ido2 = input("2. Kérek egy időt 'óra:perc:mp' formátumban: ")

    ido1_l = ido1.split(":")
    ido2_l = ido2.split(":")

    if len(ido1_l) < 3 or (len(ido2_l)) < 3:
        while len(ido1_l) < 3 or (len(ido2_l)) < 3:
            print("Hibás idő formátum!")
            ido1 = input("1. Kérek egy időt 'óra:perc:mp' formátumban: ")
            ido2 = input("2. Kérek egy időt 'óra:perc:mp' formátumban: ")
            ido1_l = ido1.split(":")
            ido2_l = ido2.split(":")

    eltelt_ido = []

    if int(ido1_l[0] <= ido2_l[0]):
        if int(ido1_l[1] < ido2_l[1]):
            ervenyes_idokoz = True
        elif int(ido1_l[1] == ido2_l[1]):
            if int(ido1_l[2] < ido2_l[2]):
                ervenyes_idokoz = True

    while not (ervenyes_idokoz):
        ido2 = input("HIBA! 2. Kérek egy időt 'óra:perc:mp' formátumban, ami későbbi, mint az 1. idő: ")
        ido2_l = ido2.split(":")
        if int(ido1_l[0] <= ido2_l[0]):
            if int(ido1_l[1] < ido2_l[1]):
                ervenyes_idokoz = True
            elif int(ido1_l[1] == ido2_l[1]):
                if int(ido1_l[2] < ido2_l[2]):
                    ervenyes_idokoz = True

    for i in range(len(ido1_l)):
        eltelt_ido.append(int(ido2_l[i]) - int(ido1_l[i]))

    print(f"A két időpont között eltelt idő: {eltelt_ido[0]}:{eltelt_ido[1]}:{eltelt_ido[2]}")
