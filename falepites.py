def feladat():
    kisfalak_szama = int(input("s: "))
    nagyfalak_szama = int(input("b: "))
    fal = int(input("w: "))

    b_magassag = nagyfalak_szama * 5

    kimenet = False

    if b_magassag > 0:
        maradek = fal % 5  # elosztva 5-el mennyi marad
        hanyszor = fal // 5  # hanyszor van meg a fal 5-ben
        if nagyfalak_szama >= hanyszor:
            if kisfalak_szama >= maradek:
                kimenet = True
        elif (fal - b_magassag) <= kisfalak_szama:
            kimenet = True

        if b_magassag % fal == 0:  # ha fal-ben pontosan meg van a b_m
            kimenet = True

    if kisfalak_szama >= fal:
        kimenet = True


    print(kimenet)
