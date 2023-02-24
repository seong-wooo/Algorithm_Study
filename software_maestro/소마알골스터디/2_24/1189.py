import sys

input = sys.stdin.readline

r, c, k  = map(int, input().split())

maps = [list(input().rstrip()) for i in range(r)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def dfs(y, x, count):
    if y == 0 and x == c - 1:
        return 1 if count == k else 0

    result = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and maps[ny][nx] != "T":
            visited[ny][nx] = True
            result += dfs(ny, nx, count + 1)
            visited[ny][nx] = False

    return result


visited = [[False] * c for _ in range(r)]
visited[r - 1][0] = True
print(dfs(r -1, 0, 1))