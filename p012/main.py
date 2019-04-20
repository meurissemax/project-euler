def count(number):
    n = 0

    i = 1

    while i * i < number:
        if (number % i) == 0:
            n += 2

        i += 1

    return n

if __name__ == '__main__':
    triangle = 1
    limit = 500

    i = 2

    while count(triangle) <= limit:
        triangle += i
        i += 1

    print(triangle)
