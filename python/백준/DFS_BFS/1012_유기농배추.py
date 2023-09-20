# 처음에 dfs 로 구현했을 때 recursion error가 발생했다.
# 재귀함수를 너무 많이 호출한 듯하다.
# 따라서 bfs로 구현을 변경하였다.
# 웬만하면 bfs로 구현하자
# 아니면 sys.setrecursionlimit(10**6) 를 코드에 추가하자.
# sys.setrecursionlimit(10**6)를 추가한 dfs 코드가 훨씬 빠르게 동작했다.




import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1


    def bfs(x, y):
        queue =deque()
        queue.append((x,y))
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while queue:
            x, y = queue.popleft()
            for index in range(4):
                nx = x + dx[index]
                ny = y + dy[index]
                if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
                    continue

                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((nx,ny))



    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1
                bfs(x, y)
                count += 1
    print(count)

# dfs 코드
# 더 빠르다.
# import sys
# sys.setrecursionlimit(10**6)
# t = int(sys.stdin.readline())
#
# for i in range(t):
#     m, n, k = map(int, sys.stdin.readline().split())
#
#     graph = [[0] * m for _ in range(n)]
#     visited = [[0] * m for _ in range(n)]
#
#     for j in range(k):
#         x, y = map(int, sys.stdin.readline().split())
#         graph[y][x] = 1
#
#
#     def dfs(x, y):
#         dx = [0, 0, 1, -1]
#         dy = [1, -1, 0, 0]
#         for index in range(4):
#             nx = x + dx[index]
#             ny = y + dy[index]
#             if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
#                 continue
#             if graph[ny][nx] == 1 and visited[ny][nx] == 0:
#                 visited[ny][nx] = 1
#                 dfs(nx, ny)
#
#
#     count = 0
#     for y in range(n):
#         for x in range(m):
#             if graph[y][x] == 1 and visited[y][x] == 0:
#                 visited[y][x] = 1
#                 dfs(x, y)
#                 count += 1
#     print(count)