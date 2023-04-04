def odejmowanko(liczba_A, liczba_B):
    if len(liczba_A) > len(liczba_B):
        buff = liczba_B
        liczba_B = liczba_A
        liczba_A = buff
    elif len(liczba_A) == len(liczba_B):
        for i in range(len(liczba_A)):
            if int(liczba_A[i]) > int(liczba_B[i]):
                buff = liczba_B
                liczba_B = liczba_A
                liczba_A = buff
                break
            elif int(liczba_A[i]) < int(liczba_B[i]):
                break
            else:
                pass

    c1 = len(liczba_A) - 1
    roznica_dlugosci = len(liczba_B) - len(liczba_A)

    odejmij_1 = False
    zapis_C = open("liczba_C.txt", "a")

    for _ in range(len(liczba_A)):
        roznica_czesciowa = int(liczba_B[c1 + roznica_dlugosci]) - int(liczba_A[c1]) - odejmij_1
        if roznica_czesciowa < 0:
            odejmij_1 = True
            zapis_C.writelines([str(roznica_czesciowa + 10)])
        else:
            odejmij_1 = False
            zapis_C.writelines([str(roznica_czesciowa)])
        c1 -= 1

    c2 = roznica_dlugosci - 1
    for _ in range(roznica_dlugosci):
        if int(liczba_B[c2]) - odejmij_1 < 0:
            odejmij_1 = True
            zapis_C.writelines([str(int(liczba_B[c2]) + 10 - odejmij_1)])
        else:
            zapis_C.writelines(str(int(liczba_B[c2]) - odejmij_1))
            odejmij_1 = False
        c2 -= 1

    zapis_C.close()

    zapis_C = open("liczba_C.txt", "r")
    liczba_C_odwrocona = zapis_C.read()
    zapis_C.close()
    zapis_C = open("liczba_C.txt", "w")
    zapis_C.writelines(liczba_C_odwrocona[::-1])
    zapis_C.close()

    zapis_C = open("liczba_C.txt", "r")
    liczba_z_zerami = zapis_C.read()

    liczba_C = ""
    condition = True
    for i in liczba_z_zerami:
        if i == "0" and condition:
            pass
        else:
            condition = False
            liczba_C += i

    zapis_C.close()

    zapis_C = open("liczba_C.txt", "w")
    zapis_C.writelines("")
    zapis_C.close()

    return liczba_C
