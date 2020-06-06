from num2words import num2words

def remove(string):
    string = string.replace('-', '')
    string = string.replace(' ', '')

    return string


n = 1000

print(sum(len(remove(num2words(i))) for i in range(1, n + 1)))
