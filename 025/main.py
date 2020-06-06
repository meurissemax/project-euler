a = 1
b = 1
c = a + b

count = 2

while len(str(c)) < 1000:
	count += 1

	c = a + b
	a, b = c, a

print(count)
