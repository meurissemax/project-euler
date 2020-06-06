def check(number, start, end):
    for i in range(start, end + 1):
        if (number % i) > 0:
            return False

    return True


start = 1
end = 20
number = start

while not check(number, start, end):
    number += 1

print(number)
