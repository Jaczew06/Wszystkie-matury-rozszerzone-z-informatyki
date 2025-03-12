from math import sqrt

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

plik = open("liczby.txt")
x = []
for i in plik:
    i = i.strip()
    x.append(i)

for i in x:
    if czy_pierwsza(int(i)) and czy_pierwsza(int(i[::-1])):
        print(i)
