from collections import deque

def solution(maps):    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    q = deque()
    q.append((0, 0, 1))
    n = len(maps)
    m = len(maps[0])
    
    while q:
        y, x, answer = q.popleft()
        answer += 1
        
        for i in range(4):            
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny == n - 1 and nx == m - 1 and maps[ny][nx] == 1:
                return answer
        
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append((ny, nx, answer))
            
    return -1