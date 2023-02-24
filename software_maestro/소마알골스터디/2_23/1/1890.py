import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1]
dx = [1, 0]


# visited 에는 종점까지 갈 수 있는 경로의 개수를 담는다.

def dfs(y, x):
    if y == x == n - 1:
        return 1

    if a[y][x] == 0:
        return 0

    for i in range(2):
        ny = y + dy[i] * a[y][x]
        nx = x + dx[i] * a[y][x]

        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx]:
                route = dfs(ny, nx)
                visited[ny][nx] = route

            visited[y][x] += visited[ny][nx]


    return visited[y][x]

visited = [[0] * n for _ in range(n)]
print(dfs(0, 0))