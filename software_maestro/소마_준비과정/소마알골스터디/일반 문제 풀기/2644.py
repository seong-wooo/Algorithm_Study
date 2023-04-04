import sys

input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())
graph1 = [[] for _ in range(n + 1)]
graph2 = [[0]*(n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    p, c = map(int, input().split())
    graph1[p].append(c)
    graph1[c].append(p)
    graph2[p][c] = 1
    graph2[c][p] = 1


def find(node, target):
    if node == target or graph2[node][target] > 0:
        return graph2[node][target]
    
    visited[node] = True
    for next in graph1[node]:
        if not visited[next]:

            if graph2[next][target] > 0:
                return 1 + graph2[next][target]

            dist = find(next, target)
            if dist > 0:
                return 1 + dist
    return -1
            


visited = [False] * (n + 1)
print(find(a, b))