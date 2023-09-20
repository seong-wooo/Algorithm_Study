# bfs로 8개의 경우의 수를 모두 조사한다.
# 3804ms로 되게 오랜 시간이 걸렸다.
# 68ms 밖에 안걸린 코드가 있다.
# 내 코드와 차이점을 확인해보자 -> 잘 모르겠다.



import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    L = int(sys.stdin.readline())
    # 현재 위치 a, b
    y, x = map(int, sys.stdin.readline().split())
    n, m = map(int, sys.stdin.readline().split())
    visited = [[0] * L for _ in range(L)]
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        if visited[n][m] != 0:
            print(visited[n][m] - 1)
            break

        y, x = queue.popleft()
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < L and 0 <= ny < L and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))







