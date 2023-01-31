import sys


def bfs(soon, visited, c, i):
    visited[i] = c
    while visited[soon[i]] == 0:
        visited[soon[i]] = c
        i = soon[i]

    return 1 if visited[soon[i]] == c else 0


for _ in range(int(sys.stdin.readline())):
    n, soon = int(sys.stdin.readline()), [0] + list(map(int, sys.stdin.readline().split()))

    visited = [0] * (n + 1)
    result = 0
    for i in range(1, n + 1):
        if not visited[i]:
            result += bfs(soon, visited, 1, i)
    print(result)
