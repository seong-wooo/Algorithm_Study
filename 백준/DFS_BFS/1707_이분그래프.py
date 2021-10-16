# 메인 아이디어: 한 노드에서 같은 거리만큼 떨어진 노드끼리는 인접하면 안된다.
# 처음에  2차원 배열로 graph를 구현했으나 메모리 초과가 발생했다
# 따라서 dictionary를 이용하여 필요한 만큼만 데이터를 삽입했다.

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    v, e  = map(int, input().split())
    graph = {}
    visited =[0] *(v+1)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        if v2 in graph:
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]

    queue = deque()

    for j in graph:
        isBGraph = True
        if visited[j] == 0:
            visited[j] = 1
            queue.append(j)
            while queue:
                V =queue.popleft()
                for k in graph[V]:
                    if visited[k] == 0:
                        visited[k] = visited[V] + 1
                        queue.append(k)
                    elif visited[k] == visited[V]:
                        isBGraph = False
                        break
                if isBGraph == False:
                    break
        if isBGraph == False:
            break
    if isBGraph:
        print("YES")
    else:
        print("NO")


