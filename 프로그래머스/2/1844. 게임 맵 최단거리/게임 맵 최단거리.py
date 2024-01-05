from collections import deque

def solution(maps):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    q = deque([(0, 0, 1)])
    maps[0][0] = 1
    
    t_y = len(maps) - 1
    t_x = len(maps[0]) - 1
    

    while q:

        y, x, count = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny == t_y and nx == t_x:
                return count + 1
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append((ny, nx, count + 1))
                
    return -1