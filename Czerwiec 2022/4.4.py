plik = open("liczby.txt")
x = []
indeksy = [0]*20000
for i in plik:
    i = i.strip()
    x.append(i)
    wszystkie = len(set(x))
    x = sorted(x)


powtorzone_dwa_razy = 0
powtorzone_trzy_razy = 0
for a in x:
    indeksy[int(a)] += 1
for i in range(len(indeksy)):
    if indeksy[i] == 2:
        powtorzone_dwa_razy += 1
    if indeksy[i] == 3:
        powtorzone_trzy_razy += 1


print(wszystkie,powtorzone_dwa_razy, powtorzone_trzy_razy)





# powtorzone_dwa_razy = 0
# for i in range(0, ):
#     if x[i] == x[i+1]:
#         powtorzone_dwa_razy += 1
#     if x[i] == x[i+2]:
#         powtorzone_dwa_razy -= 1
#         a += 2