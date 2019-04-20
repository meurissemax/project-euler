def check(number):
    inverse = 0
    n = number

    while n != 0:
        inverse = inverse * 10 + n % 10
        n = n // 10

    if number == inverse:
        return True
    else:
        return False

if __name__ == '__main__':
    max = max(i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if check(i * j))

    print(max)
