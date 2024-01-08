from collections import defaultdict
from heapq import heappop, heappush

def solution(N, road, K):
    graph = defaultdict(list)
    q = []
    for a, b, c in road:
        if c <= K:
            graph[a].append((b, c))
            graph[b].append((a, c))
    
    invalid_d = K + 1
    distance = [0, 0] + [invalid_d] * (N - 1)
    
    for b, c in graph[1]:
        if c <= K:
            heappush(q, (c, b))

    answer = 1
    while q:
        c, b = heappop(q)
        if distance[b] == invalid_d:
        
            distance[b] = c

            for next_node, value in graph[b]:
                next_value = value + c
                if distance[next_node] == invalid_d and next_value <= K:
                    heappush(q, (next_value, next_node))
            answer += 1
        
    return answer
        
    
    