import sys
from collections import defaultdict
from heapq import heappush
from heapq import heappop

input = sys.stdin.readline

n, m = map(int, input().split())

sights = list(map(int, input().split())) # 0이면 시야 x, 1이면 시야 o / 마지막은 시야 있지만 갈 수 있음
graph = defaultdict(list) # 시간, 노드
INF = 1e9
durations = [INF] * n

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

# 마지막 노드에서 출발하기

q = []
start_second = 0
heappush(q, (start_second, n - 1))
durations[n - 1] = start_second

visited = [False] * n

while q:
    duration, node = heappop(q)
    if not visited[node]:
        visited[node] = True
        durations[node] = duration

        for second, next_node in graph[node]:
            if not sights[next_node]:
                heappush(q, (duration + second, next_node))

if durations[0] == INF:
    print(-1)
else:
    print(durations[0])


