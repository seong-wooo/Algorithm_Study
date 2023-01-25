n = int(input())

if n % 2 == 1:
    print("0")
else:
    d = [0] * (n + 1)
    d[2] = 3

    for i in range(4, n + 1, 2):
        d[i] += 3 * d[i - 2]
        for j in range(4, i, 2):
            d[i] += 2 * d[i - j]
        d[i] += 2

    print(d[n])