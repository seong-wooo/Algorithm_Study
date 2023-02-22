import sys
from collections import deque


def change(num):
    return str(num - 2) if num else "0"


input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

def find_2():
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 2:
                return y, x

# y, x  -> 2인 좌표

q = deque()
q.append(find_2())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
            maps[ny][nx] = maps[y][x] + 1
            q.append((ny, nx))

for land in maps:
    print(" ".join(map(change, land)))