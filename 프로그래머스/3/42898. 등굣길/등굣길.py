from collections import deque

def solution(m, n, puddles):
    visited = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        visited[puddle[1] - 1][puddle[0] - 1] = -1
        
        
    q = deque()
    s = set()
    q.append((0, 0))
    s.add((0,0))
    
    visited[0][0] = 1
    dy = [0, 1]
    dx = [1, 0]
    
    while q:
        y, x = q.popleft()
        
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] != -1:
                visited[ny][nx] += visited[y][x]
                if (ny, nx) not in s:
                    q.append((ny, nx))
                    s.add((ny, nx))
    
    return visited[n-1][m-1] % 1000000007