

def solution(m, n, board):
    board = list(map(list, list(zip(*board))))
    return remove(board)

def remove(board):  
    answer = 0
    delete = set()
    n = len(board)
    m = len(board[0])

    for j in range(n - 1):
        for i in range(m - 1):
            if board[j][i]:
                if is_square(board, j, i):
                    delete.add((j, i))
                    delete.add((j, i + 1))
                    delete.add((j + 1, i))
                    delete.add((j + 1, i + 1))
                    
    
    if not delete:
        return answer
    
    answer += len(delete)
    for y, x in delete:
        board[y][x] = ""
    
    for y in range(len(board)):
        b = list("".join(board[y]))
        board[y] = [""] * (m - len(b)) + b
    
    return answer + remove(board)
        
    
        
        
    
def is_square(board, y, x):
    dy = [0, 1, 1]
    dx = [1, 1, 0]
    
    target = board[y][x]
    if not target:
        return False
    
    for i in range(3):
        if target != board[y+dy[i]][x+dx[i]]:
            return False
        
    return True
            
    
    
                
                
                