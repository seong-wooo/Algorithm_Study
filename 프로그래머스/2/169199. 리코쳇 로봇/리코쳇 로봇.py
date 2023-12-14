from collections import deque

def solution(board):
    r_y = 0
    r_x = 0
    g_y = 0 
    g_x = 0
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[j][i] == "R":
                r_y = j
                r_x = i
            
            if board[j][i] == "G":
                g_y = j
                g_x = i
                
    q = deque()
    q.append((r_y, r_x, 0))
    
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[r_y][r_x] = True
    
    while q:
        r_y, r_x, count = q.popleft()
        count += 1
        
        for i in range(4):
            n_y, n_x = r_y, r_x
            while 0 <= n_y + dy[i] < len(board) and 0 <= n_x + dx[i] < len(board[0]) and board[n_y + dy[i]][n_x + dx[i]] != "D":
                n_y += dy[i]
                n_x += dx[i]
            
            if (n_y, n_x) == (g_y, g_x):
                return count
            
            if not visited[n_y][n_x]:
                visited[n_y][n_x] = True
                q.append((n_y, n_x, count))
    return -1                
            
            
            
            
        
