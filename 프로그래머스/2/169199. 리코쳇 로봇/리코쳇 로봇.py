from collections import deque

def solution(board):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    
    q = deque()
    
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[j][i] == "R":
                visited[j][i] = True
                q.append((j, i, 0))
                
                while q:
                    y, x, count = q.popleft()
                    
                    for k in range(4):
                        ny = y
                        nx = x
                        
                        while 0 <= ny + dy[k] < len(board) and 0 <= nx + dx[k] < len(board[0]) and board[ny+dy[k]][nx+dx[k]] != "D":
                            ny += dy[k]
                            nx += dx[k]
                        
                        if not visited[ny][nx]:
                            if board[ny][nx] == "G":
                                return count + 1
                            visited[ny][nx] = True
                            q.append((ny, nx, count+1))
    return -1