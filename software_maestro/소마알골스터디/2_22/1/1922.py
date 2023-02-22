import sys
import heapq

def find_p(x):
    if x != parent[x]:
        parent[x] = find_p(parent[x])
    return parent[x]


def union(a, b):
    a = find_p(a)
    b = find_p(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a



input = sys.stdin.readline

n = int(input())
m = int(input())
com = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    com.append((cost, a, b))

parent = [i for i in range(n + 1)]

heapq.heapify(com)

result = 0
edge = 0
while com and edge < n:
    cost, a, b = heapq.heappop(com)
    if find_p(a) != find_p(b):
        union(a, b)
        result += cost
        edge += 1

print(result)
