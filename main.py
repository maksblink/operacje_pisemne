from dzialania.dodawanie import dodawanko
from dzialania.dzielenie import dzielonko
from dzialania.mnozenie import mnozonko
from dzialania.odejmowanie import odejmowanko

if __name__ == '__main__':
    liczba = dodawanko("270000000000000000000000000000", "3")
    print(liczba)
    liczba = mnozonko("0", "1")
    print(liczba)
    liczba = odejmowanko("1999999999999999999999", "8")
    print(liczba)
    liczba = dzielonko("3", "999")
    print(liczba)
