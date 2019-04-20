def check(number):
    if number == 2:
        return True

    i = 2

    while i * i < number + 1:
        if (number % i) == 0:
            return False

        i += 1

    return True

if __name__ == '__main__':
    n = 2000000
    sum = 0

    for i in range(2, n):
        if check(i):
            sum += i

    print(sum)
