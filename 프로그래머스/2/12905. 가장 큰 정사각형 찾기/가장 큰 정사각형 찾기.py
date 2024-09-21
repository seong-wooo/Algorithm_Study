def solution(board):
    
    for j in range(1, len(board)):
        for i in range(1, len(board[0])):
            if board[j][i] != 0:
                board[j][i] += min(board[j-1][i], board[j][i-1], board[j-1][i-1])
    
    answer = 0
    
    for b in board:
        answer = max(answer, max(b))
    

    return answer ** 2