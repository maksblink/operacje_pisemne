from dzialania.dodawanie import dodawanko
from dzialania.odejmowanie import odejmowanko


def dzielonko(liczba_A, liczba_B):
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

    zapis_D = open("liczba_D.txt", "w")
    zapis_D.writelines("1")
    zapis_D.close()

    while True:
        liczba_B = odejmowanko(liczba_A, liczba_B)

        # print(liczba_B)

        if liczba_B == "":
            break
        else:
            liczba_E = open("liczba_D.txt", "r").read()
            wynik_dodawania = dodawanko("1", liczba_E)
            zapis_D = open("liczba_D.txt", "w")
            zapis_D.writelines(wynik_dodawania)
            zapis_D.close()

    zapis_D = open("liczba_D.txt", "r")
    liczba_D = zapis_D.read()
    zapis_D.close()
    zapis_D = open("liczba_D.txt", "w")
    zapis_D.writelines("")
    zapis_D.close()

    return liczba_D
