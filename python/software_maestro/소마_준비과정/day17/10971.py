import sys

input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

mi = sys.maxsize


def dfs(visited, now, seq, cost):
    result = sys.maxsize
    if seq == n:
        if not w[now][0]:
            return sys.maxsize
        return cost + w[now][0]

    for i in range(n):
        if not visited[i] and w[now][i]:
            visited[i] = True
            result = min(result, dfs(visited, i, seq + 1, cost + w[now][i]))
            visited[i] = False
    return result


visited = [True] + [False] * (n - 1)

print(dfs(visited, 0, 1, 0))