import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [set() for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    indegree[b] += 1

q = []
for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, i)

result = []
while q:
    node = heapq.heappop(q)
    result.append(node)

    for linked_node in graph[node]:
        indegree[linked_node] -= 1
        if not indegree[linked_node]:
            heapq.heappush(q, linked_node)

print(*result)




