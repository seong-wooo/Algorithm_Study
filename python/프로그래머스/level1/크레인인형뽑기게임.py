from collections import deque


def solution(board, moves):
    result = 0
    stack = deque([0])
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] > 0:
                if stack[-1] == board[j][i - 1]:
                    stack.pop()
                    result += 2

                else:
                    stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return result