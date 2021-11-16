# 오랜만에 bfs 문제 풀어서 어렵게 느껴졌다.
# nx ny에 대해 어차피 넣고 범위 검사할거라면 범위 검사를 하고 넣는것이 더 빠르게 작동할 것이다.
# 먼저 검사를 하면 append 횟수를 줄일 수 있기 때문에

import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())

table = [[0] * n for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            table[i][j] = 1

square_list = []
queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(m):
    for j in range(n):
        if table[i][j] == 0:
            queue.append((i,j))
            square = 0
            while queue:
                y, x = queue.popleft()
                if 0<=y<m and 0<=x<n:
                    if table[y][x] == 0:
                        square += 1
                        table[y][x] = 1
                        for a in range(4):
                            queue.append((y+dy[a], x+dx[a]))
            square_list.append(square)

square_list.sort()
print(len(square_list))
for i in square_list:
    print(i, end=" ")









#먼저 검사를 하는 코드 -> 동작 시간은 똑같다 . .
import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())

table = [[0] * n for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            table[i][j] = 1

square_list = []
queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(m):
    for j in range(n):
        if table[i][j] == 0:
            queue.append((i,j))
            square = 1
            table[i][j] = 1
            while queue:
                y, x = queue.popleft()
                for a in range(4):
                    ny = y + dy[a]
                    nx = x + dx[a]
                    if 0<=ny<m and 0<=nx<n and table[ny][nx] == 0:
                        square += 1
                        table[ny][nx] = 1
                        queue.append((ny, nx))
            square_list.append(square)

square_list.sort()
print(len(square_list))
for i in square_list:
    print(i, end=" ")