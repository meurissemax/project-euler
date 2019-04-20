def check(a, b, c):
    if a < b and b < c:
        a *= a
        b *= b
        c *= c

        sum = a + b

        if sum == c:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    n = 1000

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            k = 1000 - i - j

            if check(i, j, k):
                print(i * j * k)
