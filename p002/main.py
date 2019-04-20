limit = 4000000

a = 1
b = 2

sum = 2

while a + b <= limit:
    c = a + b
    a = b
    b = c

    if (c % 2) == 0:
        sum += c

print(sum)
