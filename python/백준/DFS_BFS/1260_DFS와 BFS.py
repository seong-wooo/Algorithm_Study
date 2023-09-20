# 처음 방법 -> 딕셔너리를 이용한 그래프
# 해결 방법 -> 2차원 배열을 이용한 그래프
# 딕셔너리를 이용한 그래프는 작은 순서대로 방문하기 위해서
# 매번 정렬을 해야하므로 시간이 좀 더 걸린다.
# 각각을 시간 측정 해본 결과: 마땅한 예가 없어 포기..


import time
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0 for _ in range(n + 1)]
visited2 = visited[:]


def dfs(v):
    if visited[v] == 1:
        return
    visited[v] = 1
    print(v, end=" ")

    for i in range(1,n + 1):
        if graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        if visited2[v] == 1:
            continue
        visited2[v] = 1
        print(v, end=" ")

        for i in range(1, n + 1):
            if graph[v][i] == 1:
                queue.append(i)
# start_time = time.time() # 측정 시작
dfs(v)
print()
bfs(v)
# end_time = time.time() # 측정 종료
# print("2차원 배열 그래프 time:", end_time - start_time) # 수행 시간 출력


# graph = {}
#
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     if a not in graph:
#         graph[a] = [b]
#     else:
#         graph[a].append(b)
#
#     if b not in graph:
#         graph[b] = [a]
#     else:
#         graph[b].append(a)
#
# visited = [0 for _ in range(n + 1)]
# visited2 = visited[:]
#
#
# def dfs2(v):
#     if visited[v] == 1:
#         return
#     visited[v] = 1
#     print(v, end=" ")
#     graph_v = sorted(graph[v])
#     for i in graph_v:
#         dfs2(i)
#
#
# def bfs2(v):
#     queue = deque()
#     queue.append(v)
#
#     while queue:
#         v = queue.popleft()
#         if visited2[v] == 1:
#             continue
#         visited2[v] = 1
#         print(v, end=" ")
#         graph_v = sorted(graph[v])
#         for i in graph_v:
#             queue.append(i)
#
# start_time2 = time.time() # 측정 시작
# dfs2(v)
# print()
# bfs2(v)
# end_time2 = time.time() # 측정 종료
# print("딕셔너리 그래프 time:", end_time2 - start_time2) # 수행 시간 출력

