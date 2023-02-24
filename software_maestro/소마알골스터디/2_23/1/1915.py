import sys

n, m = map(int, input().split())
a = [[0] * (m + 1)] + [[0] + list(map(int, list(input().rstrip()))) for _ in range(n)]

answer = 0
for j in range(1, n + 1):
    for i in range(1, m + 1):
        if a[j][i] == 1:
            a[j][i] = min(a[j][i - 1], a[j - 1][i - 1], a[j - 1][i]) + 1
            answer = max(a[j][i], answer)

print(answer**2)