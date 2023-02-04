import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    graph = [set() for i in range(n + 1)]
    for i in range(n - 1):
        graph[t[i]] = set(t[i + 1:])

    change = [tuple(map(int, input().split())) for _ in range(int(input()))]

    for c in change:
        a, b = c
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].add(a)

        else:
            graph[b].remove(a)
            graph[a].add(b)


    indegree = [0] * (n + 1)
    for g in graph:
        for i in g:
            indegree[i] += 1

    q = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for linked_node in graph[node]:
            indegree[linked_node] -= 1
            if not indegree[linked_node]:
                q.append(linked_node)

    if len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")