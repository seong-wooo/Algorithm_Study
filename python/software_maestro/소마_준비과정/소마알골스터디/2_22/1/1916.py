# 다익스트라

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    bus[a].append((cost, b))

a, b = map(int, input().split())

heapq.heapify(bus[a])

INF = int(1e9)
d = [INF] * (n + 1)
d[a] = 0


while bus[a]:
    cost, dest = heapq.heappop(bus[a])

    if dest == b:
        print(cost)
        break

    if d[dest] > cost:
        d[dest] = cost
        for i in bus[dest]:
            heapq.heappush(bus[a], (cost + i[0], i[1]))
