def divisor(n):
    div = list()

    for i in range(1, int((n / 2) + 1)):
        if n % i == 0:
            div.append(i)

    return div

if __name__ == '__main__':
    n = 10000

    s, a = list(), list()
    temp = [0, 0]

    for i in range(1, n + 1):
        s.append(sum(divisor(i)))

    for i in range(0, n):
        temp[0] = i + 1

        if temp[0] not in a:
            for j in range(temp[0], n):
                temp[1] = j + 1

                if temp[1] not in a:
                    if s[i] == temp[1] and s[j] == temp[0]:
                        a.append(temp[0])
                        a.append(temp[1])

    print(sum(a))
