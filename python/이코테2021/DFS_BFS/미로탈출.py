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

# 미로탈출
# bfs로 구현해보자
# nx, ny를 이용한 bfs

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문 시에만 최단 거리 기록

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

            if graph[n - 1][m - 1] != 1:
                return graph[n - 1][m - 1]
    return graph[n - 1][m - 1]


print(bfs(0, 0))







