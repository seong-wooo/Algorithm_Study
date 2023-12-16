# 출발 -> 레버 -> 문
# 두 번의 bfs를 돌리자
# 1. 출발 to 레버
# 2. 레버 to 문 
from collections import deque

def solution(maps):
    start = ()
    lebber = ()
    exit = ()
    
    
    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i] == "S":
                start = (j, i)
            elif maps[j][i] == "L":
                lebber = (j, i)
            elif maps[j][i] == "E":
                exit = (j, i)
    
    first = bfs(start, lebber, maps)
    if first == -1:
        return -1
    
    second = bfs(lebber, exit, maps)
    
    if second == -1:
        return -1
    
    return first + second
    

def bfs(start, end, maps):
    s_y, s_x = start
    e_y, e_x = end
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    q = deque()
    q.append((s_y, s_x, 0))
    visited[s_y][s_x] = True
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    
    while q:
        y, x, count = q.popleft()
        
        count += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (ny, nx) == (e_y, e_x):
                return count
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "X":
                visited[ny][nx] = True
                q.append((ny, nx, count))
    
    return -1
    
                
                
                
            
        
        
    
    
    
    
    