n, k = map(int, input().split())

d = [[i for i in range(1, k + 1)]] + [[1] + [0] * (k - 1) for _ in range(n - 1)]

for i in range(1, n):
    for j in range(1, k):
        d[i][j] = d[i - 1][j] + d[i][j - 1]

print(d[-1][-1] % 1000000000)

