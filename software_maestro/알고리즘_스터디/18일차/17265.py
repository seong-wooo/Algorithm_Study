import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

maps = [input().split() for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

y_x_value = deque()

start = maps[0][0]
y_x_value.append((0, 0, start))

INF = 1e9
result_max = -INF
result_min = INF
while y_x_value:
    y, x, value = y_x_value.popleft()

    if y == n - 1 and x == n - 1:
        value = int(value)
        result_max = max(value, result_max)
        result_min = min(value, result_min)
        continue

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < n and nx < n:
            command = maps[ny][nx]
            if command.isdigit():
                new_value = str(eval(value + command))
            else:
                new_value = value + maps[ny][nx]
            y_x_value.append((ny, nx, new_value))

print(result_max, result_min)





