n = 1000
a = 3
b = 5

sum = 0

for i in range(n):
    if (i % a) == 0 or (i % b) == 0:
        sum += i

print(sum)
