from dzialania.dodawanie import dodawanko
from dzialania.dzielenie import dzielonko
from dzialania.mnozenie import mnozonko
from dzialania.odejmowanie import odejmowanko

if __name__ == '__main__':
    liczba = dodawanko("2700000000000000000", "3")
    print(liczba)
    liczba = mnozonko("99999", "23432451")
    print(liczba)
    liczba = odejmowanko("19999999999", "8")
    print(liczba)
    liczba = dzielonko("3", "99")
    print(liczba)
