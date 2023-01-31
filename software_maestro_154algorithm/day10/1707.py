import sys
from collections import deque


def bfs(graph, i):
    q = deque([i])
    visited[i] = True
    depth[i] = 1

    while q:
        front = q.popleft()
        for li in graph[front]:
            if not visited[li]:
                q.append(li)
                visited[li] = True
                depth[li] = depth[front] + 1
            else:
                if (depth[li] - depth[front]) % 2 == 0:
                    return False
    return True

for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    for x in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (v + 1)
    depth = [0] * (v + 1)
    depth_error = False
    for i in range(1, v + 1):
        if not visited[i]:
            result = bfs(graph, i)
            if not result:
                break
    print("YES" if result else "NO")