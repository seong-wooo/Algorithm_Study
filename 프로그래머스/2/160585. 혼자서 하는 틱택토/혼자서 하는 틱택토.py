# O는 X와 같거나 1개 더 많다.
# 2개 이상의 line은 만들어질 수 없다. 
# 2개의 line이 만들어지는 예외 -> O가 5개 X가 4개인 경우

def solution(board):
    o, x = count_ox(board)
    o_line, x_line = find_line(board)
    
    a = o_line == 0 and x_line == 0
    b = o_line == 1 and x_line == 0
    c = o_line == 0 and x_line == 1
    d = o_line == 2 and x_line == 0
    
    print(o, x, o_line, x_line)
    if a and o in (x, x + 1):
        return 1
    
    if b and (o in (3, 4) and x == o - 1):
        return 1

    if c and o == x:
        return 1
    
    if d and (o, x) == (5, 4):
        return 1
    return 0
    
    
#     if o_count >= 6 or x_count >= 5:
#         return 0
    
#     if o_count not in (x_count, x_count + 1):
#         return 0
    
#     o_line, x_line = find_line(board)
    
#     if o_line >= 1 and x_line >= 1:
#         return 0
    
#     return 1
        
    
def count_ox(board):
    o_count = 0
    x_count = 0
    for b in board:
        o_count += b.count('O')
        x_count += b.count('X')
    
    return o_count, x_count


def find_line(board):
    o_result = 0
    x_result = 0
    lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    
    for line in lines:
        a, b, c = line
        if board[a//3][a%3] == board[b//3][b%3] == board[c//3][c%3]:
            if board[a//3][a%3] == "O":
                o_result += 1
            elif board[a//3][a%3] == "X":
                x_result += 1
    
    return o_result, x_result
