# 기본적인 bfs 큐를 이용한 방법으로 풀었다.
# 

from collections import deque


def solution(n, computers):
    network = 0
    visited = [0] * n
    queue = deque()
    for i in range(n):
        if visited[i] == 0:
            queue.append(i)
            network += 1
            visited[i] = 1
            while queue:
                com = queue.popleft()
                for j in range(n):
                    if computers[com][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        queue.append(j)

    return network