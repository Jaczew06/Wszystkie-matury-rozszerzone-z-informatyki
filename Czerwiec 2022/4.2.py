plik = open("liczby.txt")
x = []
najwieksza_roznica = 0
najwieksza_liczba = 0
for i in plik:
    i = i.strip()
    x.append(i)
for i in x:
    odbicie = i[::-1]
    roznica = abs(int(i) - int(odbicie))
    if najwieksza_roznica < roznica:
        najwieksza_roznica = roznica
        najwieksza_liczba = i
print(najwieksza_liczba, najwieksza_roznica)
