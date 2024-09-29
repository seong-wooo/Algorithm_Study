from heapq import heappush, heappop
from collections import defaultdict

def solution(N, road, K):
    graph = defaultdict(list)
    
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    distance = [K+1] * (N+1)
    distance[1] = 0
    q = []
    
    
    for next_node, next_distance in graph[1]:
        heappush(q, (next_distance, next_node))
        
    while q:
        dist, node = heappop(q)
        
        if distance[node] > dist:
            distance[node] = dist

            for next_node, next_dist in graph[node]:
                if distance[next_node] > dist + next_dist:
                    heappush(q, (dist + next_dist, next_node))
        
    return sum(1 for d in distance if K >= d)