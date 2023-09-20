# heapq 라이브러리를 이용하여 해결
# heapq 라이브러리에 대한 공부를 다시 하자
import heapq
import sys

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)


