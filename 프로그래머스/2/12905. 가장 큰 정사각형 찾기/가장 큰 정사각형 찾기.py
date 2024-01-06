def solution(board):
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    answer = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            dp[y+1][x+1] = 0 if board[y][x] == 0 else board[y][x] + min(dp[y][x], dp[y][x+1], dp[y+1][x])
            answer = max(dp[y+1][x+1], answer)
    return answer ** 2