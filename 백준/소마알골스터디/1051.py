import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rec = [list(input().rstrip()) for _ in range(n)]

max_size = 1
max_width = min(m, n)

for j in range(n):
    for i in range(m):
        for k in range(i + 1, min(m, n + i - j)):
            if rec[j][i] == rec[j][k] == rec[j + k - i][i] == rec[j + k - i][k]:
                max_size = max(max_size, (k - i + 1) ** 2)
print(max_size)