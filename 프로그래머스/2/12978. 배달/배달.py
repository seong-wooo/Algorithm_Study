from collections import defaultdict
import heapq

def solution(N, road, K):
    graph = defaultdict(list)
    q = []
    for a, b, c in road:
        if c <= K:
            graph[a].append((b, c))
            graph[b].append((a, c))
        
    INF = 1e9
    distance = [0, 0] + [INF] * (N - 1)
    
    for b, c in graph[1]:
        heapq.heappush(q, (c, b))
    
    while q:
        c, b = heapq.heappop(q)
        
        if distance[b] > c:
            distance[b] = c
            
            for next_node, next_distance in graph[b]:
                heapq.heappush(q, (c+next_distance, next_node))

    return len([d for d in distance if d<=K]) - 1