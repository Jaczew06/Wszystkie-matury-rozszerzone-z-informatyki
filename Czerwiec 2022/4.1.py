plik = open("liczby.txt")
x = []
for i in plik:
    i = i.strip()
    x.append(i)
for i in x:
    odbicie = i[::-1]
    if int(odbicie) % 17 == 0:
        print(odbicie)
