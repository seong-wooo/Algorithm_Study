import sys

n, m, k = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

bdB = [[0] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]
bdW = [[0] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0:
            if board[i][j] == 'B':
                bdW[i + 1][j + 1] = 1
            else:
                bdB[i + 1][j + 1] = 1

        elif i % 2 == 0 and j % 2 == 1:
            if board[i][j] == 'B':
                bdB[i + 1][j + 1] = 1
            else:
                bdW[i + 1][j + 1] = 1

        elif i % 2 == 1 and j % 2 == 0:
            if board[i][j] == 'B':
                bdB[i + 1][j + 1] = 1
            else:
                bdW[i + 1][j + 1] = 1

        else:
            if board[i][j] == 'B':
                bdW[i + 1][j + 1] = 1
            else:
                bdB[i + 1][j + 1] = 1

for i in range(1, n + 1):
    for j in range(2, m + 1):
        bdB[i][j] += bdB[i][j - 1]
        bdW[i][j] += bdW[i][j - 1]

for i in range(2, n + 1):
    for j in range(1, m + 1):
        bdB[i][j] += bdB[i - 1][j]
        bdW[i][j] += bdW[i - 1][j]

results = set()

for i in range(k, n + 1):
    for j in range(k, m + 1):
        a = bdB[i][j] - bdB[i][j - k] - bdB[i - k][j] + bdB[i - k][j - k]
        b = bdW[i][j] - bdW[i][j - k] - bdW[i - k][j] + bdW[i - k][j - k]
        results.add(min(a, b))

print(min(results))