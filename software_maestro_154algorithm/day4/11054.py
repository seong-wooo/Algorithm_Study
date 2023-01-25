import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

dp_up = [1] + [0] * (n - 1)
dp_down = [0] * (n - 1) + [1]

for i in range(1, n):
    up = 1
    down = 1
    for j in range(i - 1, -1, -1):
        if a[i] > a[j] and dp_up[j] >= up:
            up = dp_up[j] + 1

        if a[n - 1 - i] > a[n - 1 - j] and dp_down[n - 1 - j] >= down:
            down = dp_down[n - 1 - j] + 1

    dp_up[i] = up
    dp_down[n - 1 - i] = down

print(max([dp_up[x] + dp_down[x] - 1 for x in range(n)]))
