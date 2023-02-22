import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())  # n 가로 m 세로

war = [input().rstrip() for _ in range(m)]
visited = [[False] * n for _ in range(m)]
q = deque()

score = {"W": 0, "B" : 0}
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for j in range(m):
    for i in range(n):
        if not visited[j][i]:
            q.append((j, i))
            color = war[j][i]
            visited[j][i] = True
            color_count = 1
            while q:
                y, x = q.popleft()

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and war[ny][nx] == color:
                        visited[ny][nx] = True
                        color_count += 1
                        q.append((ny, nx))

            score[color] += color_count ** 2

print(score["W"], score["B"])