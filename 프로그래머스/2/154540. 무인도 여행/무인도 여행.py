from collections import deque

def solution(maps):
    
    q = deque()
    
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
               
    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i] != "X" and not visited[j][i]:
                visited[j][i] = True
                q.append((j, i))
                land = int(maps[j][i])
                
                while q:
                    y, x = q.popleft()
                    
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "X":
                            visited[ny][nx] = True
                            land += int(maps[ny][nx])
                            q.append((ny, nx))
                
                answer.append(land)
    
    return sorted(answer) if answer else [-1]