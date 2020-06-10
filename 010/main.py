def check(number):
    if number == 2:
        return True

    i = 2

    while i * i < number + 1:
        if (number % i) == 0:
            return False

        i += 1

    return True


n = 2000000
s = 0

for i in range(2, n):
    if check(i):
        s += i

print(s)
