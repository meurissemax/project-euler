# Open and read the file

with open('p022_names.txt', 'r') as file:
	content = file.read()

# Transform the content of the file into a list

content = content.rstrip('\n').split(',')

# Remove first and last character of each name (")

names = list(map(lambda name : name[1:-1], content))

# Sort the list of names

names.sort()

# Calculate the score of each name and the sum
# of each score

score = 0

for i, name in enumerate(names):
	name_score = 0

	for letter in name:
		name_score += ord(letter) - ord('A') + 1

	score += name_score * (i + 1)

# Display final score

print(score)
