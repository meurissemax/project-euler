n = 600851475143
factor = 2

while n != 1:
    if not n % factor:
        n /= factor

        print(factor)
    else:
        factor += 1
