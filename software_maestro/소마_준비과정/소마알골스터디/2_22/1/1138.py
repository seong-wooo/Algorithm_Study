import sys
import heapq

input = sys.stdin.readline

n = int(input())

peoples = [-1] + list(map(int, input().split()))

q = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if peoples[i] == 0:
        heapq.heappush(q, i)
        visited[i] = True

result = []

while q:
    now = heapq.heappop(q)
    result.append(now)

    peoples[1:now] = map(lambda x: x - 1 if x != 0 else 0, peoples[1:now])

    for i in range(1, now):
        if peoples[i] == 0 and not visited[i]:
            visited[i] = True
            heapq.heappush(q, i)

print(*result)