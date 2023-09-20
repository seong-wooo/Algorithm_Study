n = int(input())

c1 = [0, 1, 1, 2, 3]
for i in range(5, n + 1):
    c1.append(c1[i - 1] + c1[i - 2])

print(c1[-1], n - 2)
