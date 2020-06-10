limit = 4000000

a = 1
b = 2
c = a + b

s = 2

while c <= limit:
    c = a + b
    a, b = b, c

    if (c % 2) == 0:
        s += c

print(s)
