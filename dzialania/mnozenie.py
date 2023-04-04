from dzialania.dodawanie import dodawanko


def mnozonko(liczba_A, liczba_B):
    if len(liczba_A) > len(liczba_B):
        buff = liczba_B
        liczba_B = liczba_A
        liczba_A = buff

    for i in range(len(liczba_A)):

        liczba_do_odwrocenia = open("liczba_do_odwrocenia.txt", "a")
        dodaj = 0
        for j in range(len(liczba_B)):
            iloczyn_czesciowy = int(liczba_A[len(liczba_A) - i - 1]) * int(liczba_B[len(liczba_B) - j - 1]) + dodaj
            dodaj = 0
            if iloczyn_czesciowy > 9:
                dodaj = int(str(iloczyn_czesciowy)[0])
                liczba_do_odwrocenia.writelines(str(iloczyn_czesciowy)[1])

            else:
                liczba_do_odwrocenia.writelines(str(iloczyn_czesciowy))
        if dodaj:
            liczba_do_odwrocenia.writelines(str(dodaj))
        liczba_do_odwrocenia.close()
        liczba_do_odwrocenia = open("liczba_do_odwrocenia.txt", "r")
        liczba_nieodwrocona = liczba_do_odwrocenia.read()
        liczba_do_odwrocenia.close()

        liczba_do_odwrocenia = open("liczba_do_odwrocenia.txt", "w")
        liczba_do_odwrocenia.writelines("")
        liczba_do_odwrocenia.close()

        liczba_odwrocona = liczba_nieodwrocona[::-1]
        liczby_do_sumy = open("liczby_do_sumy.txt", "a")
        liczby_do_sumy.writelines(liczba_odwrocona)
        for _ in range(i):
            liczby_do_sumy.writelines("0")
        liczby_do_sumy.writelines("\n")

        liczby_do_sumy.close()

    liczby_do_sumy = open("liczby_do_sumy.txt", "r")

    c3 = 0
    for i in liczby_do_sumy.read():
        if i == "\n":
            c3 += 1
    liczby_do_sumy.close()

    for _ in range(c3 - 1):
        liczby_do_sumy = open("liczby_do_sumy.txt", "r")

        pierwsza_liczba = liczby_do_sumy.readline()
        # print(pierwsza_liczba[:-1])
        druga_liczba = liczby_do_sumy.readline()
        # print(druga_liczba[:-1])

        liczby_do_sumy.close()

        with open('liczby_do_sumy.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('liczby_do_sumy.txt', 'w') as fout:
            fout.writelines(data[2:])

        wynik_dodawania = dodawanko(pierwsza_liczba[:-1], druga_liczba[:-1])
        # print(wynik_dodawania)
        liczby_do_sumy = open("liczby_do_sumy.txt", "a")
        liczby_do_sumy.writelines(wynik_dodawania)
        liczby_do_sumy.writelines("\n")
        liczby_do_sumy.close()

    liczby_do_sumy = open("liczby_do_sumy.txt", "r")
    odpowiedz = liczby_do_sumy.read()[:-1]
    liczby_do_sumy.close()
    liczby_do_sumy = open("liczby_do_sumy.txt", "w")
    liczby_do_sumy.writelines("")
    liczby_do_sumy.close()

    return odpowiedz
