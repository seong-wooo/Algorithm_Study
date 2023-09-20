import sys
import heapq

input =sys.stdin.readline

t = int(input())
for i in range(t):
    min_heap = []
    max_heap = []
    k = int(input())
    visited = [False] * k
    for j in range(k):
        a, b = input().rstrip().split()

        if a == 'I':
            heapq.heappush(min_heap, (int(b), j))
            heapq.heappush(max_heap, (-int(b), j))

        else:
            if b == "-1":
                while min_heap:
                    pop = heapq.heappop(min_heap)
                    if not visited[pop[1]]:
                        visited[pop[1]] = True
                        break
                    
            else:
                while max_heap:
                    pop = heapq.heappop(max_heap)
                    if not visited[pop[1]]:
                        visited[pop[1]] = True
                        break

    result = []
    while max_heap:
        pop = heapq.heappop(max_heap)
        if not visited[pop[1]]:
            result.append(-pop[0])
            break

    if not result:
        print("EMPTY")
    else:
        while min_heap:
            pop = heapq.heappop(min_heap)
            if not visited[pop[1]]:
                result.append(pop[0])
                break

        print(result[0], result[1])