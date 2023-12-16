from collections import deque

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    q = deque()
    answer = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i] != "X" and not visited[j][i]:
                visited[j][i] = True
                q.append((j, i))
                days = int(maps[j][i])
                
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "X":
                            days += int(maps[ny][nx])
                            visited[ny][nx] = True
                            q.append((ny, nx))
                            
                answer.append(days)
    
    return sorted(answer) if answer else [-1]
            