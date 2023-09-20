import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [input().rstrip() for _ in range(n)]

visited = [[0] * m for _ in range(n)]

result = []
def calc_size(y, x, max_size):
    size = 0
    s = 1
    while s <= max_size:
        if board[y + s][x] == board[y - s][x] == board[y][x + s] == board[y][x - s] == "*":
            size += 1
            visited[y + s][x] = visited[y - s][x] = visited[y][x + s] = visited[y][x - s] = 1
            s += 1
        else:
            break

    if size != 0:
        visited[y][x] = 1
        result.append((y + 1, x + 1, size))


for j in range(n):
    for i in range(m):
        if board[j][i] == "*":
            max_size = min(i, j, n - 1 - j, m - 1 - i)
            calc_size(j, i, max_size)

def answer():
    for j in range(n):
        for i in range(m):
            if visited[j][i] == 0 and board[j][i] == "*":
                return False
    return True


if not answer():
    print("-1")
else:
    print(len(result))
    for r in result:
        print(*r)
