def generate(actual):
    if (actual % 2) == 0:
        next = actual / 2
    else:
        next = 3 * actual + 1

    return next


limit = 1000000
max = 0

for i in range(2, limit):
    size = 0
    actual = i

    while actual != 1:
        actual = generate(actual)
        size += 1

    if size > max:
        max = size
        answer = i

print(answer)
