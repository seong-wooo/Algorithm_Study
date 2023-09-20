# 최소 2개를 빼와서 다시 힙에 넣는다. 이것을 크기가 1이 될 때 까지 반복한다.
# 정렬 후 값이 작은 순서대로 더해가면 안된다.
# 두 값을 더한 후 그 값을 다시 힙에 넣고
# 다시 최솟값 2개를 찾아야한다.

import sys
import heapq

h = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
heapq.heapify(h)

result = 0

while len(h) > 1:
    pop_sum = heapq.heappop(h) + heapq.heappop(h)
    result += pop_sum
    heapq.heappush(h, pop_sum)
print(result)
