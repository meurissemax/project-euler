def factorial(n):
    f = n

    i = n - 1

    while i != 1:
        f *= i
        i -= 1

    return f

if __name__ == '__main__':
    n = 40
    k = 20

    c = factorial(n) / (factorial(k) * factorial(n - k))

    print(c)
