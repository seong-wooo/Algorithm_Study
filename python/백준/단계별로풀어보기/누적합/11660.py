import sys

n, m = map(int, sys.stdin.readline().split())

se = set()

a = [[0] * (n + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        a[y][x] += a[y][x - 1]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        a[y][x] += a[y - 1][x]

ans = []

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 -1]

    ans.append(str(result))

print("\n".join(ans))
