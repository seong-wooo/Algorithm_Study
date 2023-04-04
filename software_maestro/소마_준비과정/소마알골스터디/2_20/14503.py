import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(input().split()) for _ in range(n)]

# room이 0인 경우 -> 청소해야함, 1인 경우 -> 벽


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 0

# d 바라보고 있는 방향
# 0 북, 1 동, 2 남, 3 서
def dfs(y, x, d):
    global count

    if room[y][x] == "0":
        count += 1
        room[y][x] = "2"

    start_direction = d - 1 if d != 0 else 3

    for i in range(4):
        direction = (4 + start_direction - i) % 4

        ny = y + dy[direction]
        nx = x + dx[direction]

        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == "0":
            return dfs(ny, nx, direction)


    back_direction = (d + 2) % 4
    ny = y + dy[back_direction]
    nx = x + dx[back_direction]

    if 0 <= ny < n and 0 <= nx < m and room[ny][nx] != "1":
        dfs(ny, nx, d)


dfs(r,c,d)


print(count)
