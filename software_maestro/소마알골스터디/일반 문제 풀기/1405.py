import sys
sys.setrecursionlimit(10**6)
n, E, W, S, N = map(int, sys.stdin.readline().split())

p = [E / 100, W / 100, S / 100, N / 100]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

board = [[0] * 30 for _ in range(30)]


def dfs(y, x, move, per):
    if move == n:
        return per

    result = 0
    for i in range(4):
        if p[i] != 0:
            ny = y + dy[i]
            nx = x + dx[i]

            if board[ny][nx] != 1:
                board[ny][nx] = 1
                result += dfs(ny, nx, move + 1, per * p[i])
                board[ny][nx] = 0

    return result

board[14][14] = 1
print(dfs(14, 14, 0, 1))
