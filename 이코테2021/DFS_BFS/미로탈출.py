# 미로탈출
# bfs로 구현해보자
# 내려가는 방향, 오른쪽 방향 우선 탐색

from collections import deque

n, m = map(int, input().split())

miro = []

for _ in range(n):
    miro.append(list(map(int, input())))

bfs_q = deque()
bfs_q.append([0, 0])

while bfs_q:
    row, col = bfs_q.popleft()

    if row < n - 1 and miro[row + 1][col] == 1:
        bfs_q.append([row + 1, col])
        miro[row + 1][col] = miro[row][col] + 1
    if col < m - 1 and miro[row][col + 1] == 1:
        bfs_q.append([row, col + 1])
        miro[row][col + 1] = miro[row][col] + 1
    if col > 0 and miro[row][col - 1] == 1:
        bfs_q.append([row, col - 1])
        miro[row][col - 1] = miro[row][col] + 1
    if row > 0 and miro[row - 1][col] == 1:
        bfs_q.append([row - 1, col])
        miro[row - 1][col] = miro[row][col] + 1

    if miro[n - 1][m - 1] != 1:
        break

print(miro[n - 1][m - 1])