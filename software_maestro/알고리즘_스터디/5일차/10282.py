import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):

    n, d, c = map(int, input().split())
    dict = defaultdict(list)

    visited = [False] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        dict[b].append((a, s))

    q = []
    heapq.heappush(q, (0, c))
    result_count = 0
    result_duration = 0

    while q:
        duration, com = heapq.heappop(q)


        if not visited[com]:
            result_duration = max(result_duration, duration)
            visited[com] = True
            result_count += 1


            for next, second in dict[com]:
                next_duration = duration + second
                heapq.heappush(q, (next_duration, next))

    print(result_count, result_duration)
