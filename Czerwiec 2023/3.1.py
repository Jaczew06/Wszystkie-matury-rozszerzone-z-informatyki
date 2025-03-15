def funckja():
    rowne = 0
    rozne_o_jeden = 0

    plik = open('przyklad.txt')
    for linia in plik:
        if linia.count('0') == linia.count('1'):
            rowne += 1
        else:
            if abs(linia.count('1') - linia.count('0')) == 1:
                rozne_o_jeden += 1
    return rowne, rozne_o_jeden


print(funckja())
