def check(a, b, c):
    if a < b and b < c:
        a *= a
        b *= b
        c *= c

        s = a + b

        if s == c:
            return True

    return False


n = 1000

for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = 1000 - i - j

        if check(i, j, k):
            print(i * j * k)
