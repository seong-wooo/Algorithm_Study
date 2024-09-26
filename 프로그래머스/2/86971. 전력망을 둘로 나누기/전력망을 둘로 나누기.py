from collections import defaultdict

def solution(n, wires):

    graph = defaultdict(list)
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    children = [0] * (n + 1)
    
    find_children(1, children, visited, graph)

    return min(abs(n - 2 *(children[i] + 1)) for i in range(1, n+1))

    
def find_children(node, children, visited, graph):
    visited[node] = True
    result = 0
    for next_node in graph[node]:
        if not visited[next_node]:
            result += 1 + find_children(next_node, children, visited, graph)

    children[node] = result
    return result