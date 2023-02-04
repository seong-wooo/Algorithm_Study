import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    depth[b] += 1

q = deque()
for i in range(1, n + 1):
    if not depth[i]:
        q.append(i)

result = []
while q:
    a = q.popleft()
    result.append(a)

    for b in graph[a]:
        depth[b] -= 1
        if not depth[b]:
            q.append(b)

print(*result)