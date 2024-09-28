# 1. 아무도 안이겼을 때 -> O 개수 >= X개수
# 2. O가 이겼을 때 -> X개수 = O개수 - 1
# 3. X가 이겼을 때 -> O개수 = X개수

def solution(board):    
    o = 0
    x = 0
    for i in range(3):
        o += board[i].count("O")
        x += board[i].count("X")
    
    if o != x and o != x + 1:
        return 0
    
    is_o_bingo = is_bingo("O", board)
    is_x_bingo = is_bingo("X", board)
    
    if is_o_bingo and is_x_bingo:
        return 0
    
    if is_o_bingo:
        return 1 if o == x+1 else 0
    
    if is_x_bingo:
        return 1 if o == x else 0
    
    return 1
    
def is_bingo(shape, board):
    for j in range(3):
        if all(shape == board[j][i] for i in range(3)):
            return True
    
    for i in range(3):
        if all(shape == board[j][i] for j in range(3)):
            return True
    
    if all(shape == board[i][i] for i in range(3)):
        return True
    
    if all(shape == board[i][2-i] for i in range(3)):
        return True
    
    return False
    
    