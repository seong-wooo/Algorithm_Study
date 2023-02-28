import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

a = [[0] * (m + 1)] + [[0] + list(map(int, list(input().strip()))) for _ in range(n)]

for j in range(1, n + 1):
    for i in range(1, m + 1):
        a[j][i] += a[j][i - 1]

for j in range(1, n + 1):
    for i in range(1, m + 1):
        a[j][i] += a[j - 1][i]


# x 좌표 같은 것이 3개인 경우 -> y 좌표 3개로 나누어야함
# x 좌표 같은 것이 2개인 경우 -> ㅑ ㅕ
# y 좌표 같은 것이 3개인 경우 -> 내천
# y 좌표 같은 것이 2개인 경우 -> ㅠㅛ
def calc(x_s, x_e, y_s, y_e):
    return a[y_e][x_e] - a[y_s - 1][x_e] - a[y_e][x_s - 1] + a[y_s - 1][x_s - 1]


maximum = 0

for x1, x2 in combinations([i for i in range(1, m)], 2):
    maximum = max(
        maximum,
        calc(1, x1, 1, n) * calc(x1 + 1, x2, 1, n) * calc(x2 + 1, m, 1, n)
    )

for y1, y2 in combinations([i for i in range(1, n)], 2):
    maximum = max(
        maximum,
        calc(1, m, 1, y1) * calc(1, m, y1 + 1, y2) * calc(1, m, y2 + 1, n)
    )

# x좌표 하나, y좌표 1개 골라야함 ㅑ ㅕ ㅛ ㅠ
for j in range(1, n):
    for i in range(1, m):
        maximum = max(
            maximum,
            calc(1, i, 1, n) * calc(i + 1, m, 1, j) * calc(i + 1, m, j + 1, n),
            calc(1, i, 1, j) * calc(1, i, j + 1, n) * calc(i + 1, m, 1, n),
            calc(1, i, 1, j) * calc(i + 1, m, 1, j) * calc(1, m, j + 1, n),
            calc(1, m, 1, j) * calc(1, i, j + 1, n) * calc(i + 1, m, j + 1, n)
        )

print(maximum)
