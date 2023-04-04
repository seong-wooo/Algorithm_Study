import sys

input = sys.stdin.readline
n, m = map(int, input().split())

w = ["WB" * 4, "BW" * 4] * 4
b = ["BW" * 4, "WB" * 4] * 4

INF = int(1e9)
result = INF

a = [input().rstrip() for _ in range(n)]

for j in range(n - 7):
    for i in range(m - 7):
        w_count = 0
        b_count = 0
        for k in range(8):
            for l in range(8):
                if w[k][l] != a[k + j][l + i]:
                    w_count += 1
                if b[k][l] != a[k + j][l + i]:
                    b_count += 1
        result = min(result, w_count, b_count)

print(result)
