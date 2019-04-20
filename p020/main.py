def factorial(n):
    f = n

    i = n - 1

    while i > 1:
        f *= i
        i -= 1

    return f

if __name__ == '__main__':
    n = 100

    print(sum(map(int, str(factorial(n)))))
