def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n es par
            n = n / 2
        else:  # n es impar
            n = n * 3 + 1
        n = int(n)

sequence(3)

#sequence(8)