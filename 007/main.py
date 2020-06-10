def check(number):
    if number == 2:
        return True

    i = 2

    while i * i < number + 1:
        if (number % i) == 0:
            return False

        i += 1

    return True


n = 10001
count = 0
i = 2

while count < n:
    if check(i):
        count += 1

    i += 1

i -= 1

print(i)
