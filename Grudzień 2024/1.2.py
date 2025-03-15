def J(n):
    b = 1
    while n > 0:
        if n % 2 == 1:
            print(b)
        n = n // 2
        b = b +1
J(19)
