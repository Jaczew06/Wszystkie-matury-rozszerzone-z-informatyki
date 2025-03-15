def maksymalna_roznica_bin():
    liczby = []
    plik = open("przyklad.txt")
    for linia in plik:
        linia = linia.strip()
        liczby.append(int(linia, 2))

    maks_roznica = 0


    for i in range(len(liczby) - 1):
        roznica = abs(liczby[i] - liczby[i + 1])
        if roznica > maks_roznica:
            maks_roznica = roznica


    return bin(maks_roznica)[2:]

wynik = maksymalna_roznica_bin()
print("Największa różnica w zapisie binarnym:", wynik)
