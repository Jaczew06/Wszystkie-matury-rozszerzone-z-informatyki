from math import sqrt
plik = open("liczby.txt")
def kwadrat():
    ilosc = 0
    pierwsza = None
    for linia in plik:
        liczba = int(linia.strip())
        if sqrt(liczba).is_integer():
            ilosc += 1
            if pierwsza is None:
                pierwsza = liczba

    return ilosc, pierwsza

print(kwadrat())
