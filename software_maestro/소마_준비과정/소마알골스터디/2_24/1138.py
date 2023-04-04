import sys
import heapq

input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))

q = []

for i in range(n):
    if not line[i]:
        heapq.heappush(q, i)

result = []
while q:
    now = heapq.heappop(q)
    result.append(str(now + 1))
    for i in range(now):
        line[i] -= 1
        if not line[i]:
            heapq.heappush(q, i)



print(" ".join(result))
