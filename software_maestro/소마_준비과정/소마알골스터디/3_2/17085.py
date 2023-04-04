import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [input().rstrip() for _ in range(n)]
sizes = []
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def calc_size(y, x, max_size):
    size = 0
    s = 1
    while s <= max_size:
        if board[y + s][x] == board[y - s][x] == board[y][x + s] == board[y][x - s] == "#":
            size = s
            s += 1
        else:
            break

    return size


def calc(s1, s2):
    y1, x1, size1 = s1
    y2, x2, size2 = s2

    s = set()
    s.add((y1, x1))
    for j in range(1, size1 + 1):
        for i in range(4):
            s.add((y1 + dy[i] * j, x1 + dx[i] * j))

    if (y2, x2) in s:
        return 0

    for j in range(1, size2 + 1):
        for i in range(4):
            if (y2 + dy[i] * j, x2 + dx[i] * j) in s:
                return 0

    return (size1 * 4 + 1) * (size2 * 4 + 1)


for j in range(n):
    for i in range(m):
        if board[j][i] == "#":
            max_size = min(i, j, n - 1 - j, m - 1 - i)
            size = calc_size(j, i, max_size)
            for k in range(size + 1):
                sizes.append((j, i, k))

result = 1
for i in range(len(sizes) - 1):
    for j in range(i + 1, len(sizes)):
        result = max(result, calc(sizes[i], sizes[j]))

print(result)
