import heapq

def solution(n, costs):
    costs = [[cost[2], cost[0], cost[1]] for cost in costs]
    heapq.heapify(costs)
    
    parent = [i for i in range(n + 1)]
    answer = 0
    while costs:
        cost, a, b = heapq.heappop(costs)
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            answer += cost
    return answer


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    