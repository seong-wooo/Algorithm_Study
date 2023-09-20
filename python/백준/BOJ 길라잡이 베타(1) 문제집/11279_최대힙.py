# 최소힙과는 반대로 - 부호를 붙인 채로 push하고 pop한다.
import sys
import heapq

n = int(sys.stdin.readline())
h = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(-heapq.heappop(h) if h else "0")
    else:
        heapq.heappush(h,-x)


