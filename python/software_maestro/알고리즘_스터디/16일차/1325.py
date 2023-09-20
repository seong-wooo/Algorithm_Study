import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

count = [0] * (n + 1)

def bfs(x):
    visited = [False] * (n + 1)
    q = deque([x])
    result = 0
    visited[x] = True

    while q:
        x = q.popleft()

        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                result += 1
                q.append(y)

    return result


for x in range(1, n + 1):
    count[x] = bfs(x)

maximum = max(count)

for i in range(1, n + 1):
    if count[i] == maximum:
        print(i, end = " ")
