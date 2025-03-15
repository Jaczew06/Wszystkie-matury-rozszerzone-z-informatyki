import itertools

def Anagramy_cyfrowe():
    x = []
    max_dlugosc = 0
    najdluzsza = []
    plik = open("anagram.txt")
    for i in plik:
        i = i.strip()
        if len(i) == 8:
            x.append(i)
            permutations = set(itertools.permutations(i))
            dlugosc_permutacji = len(permutations)
            if dlugosc_permutacji > max_dlugosc:
                max_dlugosc = dlugosc_permutacji
                najdluzsza = [i]
            elif dlugosc_permutacji == max_dlugosc:
                najdluzsza.append(i)

    return najdluzsza
print(Anagramy_cyfrowe())
