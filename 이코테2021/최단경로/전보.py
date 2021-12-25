import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, loc = heapq.heappop(q)

        if dist > distance[loc]:
            continue

        for i in graph[loc]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
maxDist = 0
count = 0

for i in distance:
    if i != INF:
        count += 1
        maxDist = max(maxDist, i)
print(count - 1, maxDist)
