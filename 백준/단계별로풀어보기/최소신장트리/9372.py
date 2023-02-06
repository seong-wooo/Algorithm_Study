import sys


def dfs(index, count):
    visit[index] = 1
    for i in graph[index]:
        if not visit[i]:
            count = dfs(i, count + 1)
    return count


input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (n + 1)
    print(dfs(1, 0))


