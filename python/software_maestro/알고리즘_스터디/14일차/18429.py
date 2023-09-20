import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))


visited = [False] * n
def dfs(weight):
    if False not in visited:
        return 1

    result = 0
    for i in range(n):
        today_weight = weight + a[i] - k
        if not visited[i] and today_weight >= 0:
            visited[i] = True
            result += dfs(today_weight)
            visited[i] = False

    return result

print(dfs(0))