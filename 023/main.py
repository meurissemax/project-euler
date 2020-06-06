# Find if a number n is abundant

def abundant(n):
	divisors = [1]

	for i in range(2, int(n / 2) + 1):
		if n % i == 0:
			divisors += [i]

	return sum(divisors) > n


# General variable

limit = 28123

# Find all abundant numbers under 'limit'

abundants = []

for i in range(1, limit + 1):
	if abundant(i):
		abundants += [i]

# Get all numbers (under 'limit') which can be written as
# the sum of two abundant numbers

expressible = [False] * limit

for i in abundants:
	for j in abundants:
		if i + j < limit:
			expressible[i + j] = True

# Sum all numbers that are not in 'sum_abundants'

ans = 0

for i, x in enumerate(expressible):
	if not x:
		ans += i

# Display answer

print(ans)
