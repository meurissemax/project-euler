def generate(actual):
    if (actual % 2) == 0:
        return actual / 2
    else:
        return 3 * actual + 1


limit = 1000000
m = 0

for i in range(2, limit):
    size = 0
    actual = i

    while actual != 1:
        actual = generate(actual)
        size += 1

    if size > max:
        m = size
        answer = i

print(answer)
