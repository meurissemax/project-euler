n = 100

sum_square = 0
square_sum = 0

for i in range(1, n + 1):
    sum_square += i * i
    square_sum += i

square_sum *= square_sum

print(square_sum - sum_square)
