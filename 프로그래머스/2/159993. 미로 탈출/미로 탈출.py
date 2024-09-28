# S -> L -> E
from collections import deque
def solution(maps):
    
    y_l, x_l, count = find_l(maps)
    
    if y_l == -1:
        return -1
    
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    q.append((y_l, x_l, count))
    visited[y_l][x_l] = True
    while q:
        y, x, count = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "X":
                if maps[ny][nx] == "E":
                    return count + 1
                visited[ny][nx] = True
                q.append((ny, nx, count + 1))

    return -1
    
    
def find_l(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    
    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i] == "S":
                visited[j][i] = True
                q.append((j, i, 0))
        
                while q:
                    y, x, count = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "X":
                            if maps[ny][nx] == "L":
                                return (ny, nx, count + 1)
                            visited[ny][nx] = True
                            q.append((ny, nx, count + 1))
    return (-1,-1,-1)
                    
                    
                