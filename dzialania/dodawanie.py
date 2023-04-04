def dodawanko(liczba_A, liczba_B):
    if len(liczba_A) > len(liczba_B):
        buff = liczba_B
        liczba_B = liczba_A
        liczba_A = buff

    c1 = len(liczba_A) - 1
    roznica_dlugosci = len(liczba_B) - len(liczba_A)

    dodaj_1 = False
    zapis_C = open("liczba_C.txt", "a")

    for _ in range(len(liczba_A)):
        suma_czesciowa = int(liczba_A[c1]) + int(liczba_B[c1 + roznica_dlugosci]) + dodaj_1
        if suma_czesciowa > 9:
            dodaj_1 = True
            zapis_C.writelines([str(suma_czesciowa - 10)])
        else:
            dodaj_1 = False
            zapis_C.writelines([str(suma_czesciowa)])
        c1 -= 1

    c2 = roznica_dlugosci - 1
    for _ in range(roznica_dlugosci):
        if int(liczba_B[c2]) + dodaj_1 > 9:
            dodaj_1 = True
            zapis_C.writelines([str(int(liczba_B[c2]) + dodaj_1 - 10)])
        else:
            zapis_C.writelines(str(int(liczba_B[c2]) + dodaj_1))
            dodaj_1 = False
        c2 -= 1
    if dodaj_1:
        zapis_C.writelines("1")

    zapis_C.close()

    zapis_C = open("liczba_C.txt", "r")
    liczba_C_odwrocona = zapis_C.read()
    zapis_C.close()
    liczba_C = liczba_C_odwrocona[::-1]
    zapis_C = open("liczba_C.txt", "w")
    zapis_C.writelines("")
    zapis_C.close()

    return liczba_C
