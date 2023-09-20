# 기본적인 bfs 방식으로 구현하였다.
# 이 문제를 통해 bfs 방식이 조금 더 익숙해졌다.

from collections import deque
v = int(input())
e = int(input())

graph = [[0]*(v+1) for _ in range(v+1)]

for i in range(e):
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1


queue = deque()
queue.append(1)
visited = [0] * (v+1)
visited[1] = 1
count = 0
while queue:
  visit = queue.popleft()
  for i in range(v+1):
    if graph[visit][i] == 1 and visited[i] == 0:
      queue.append(i)
      visited[i] = 1
      count += 1

print(count)

# 조금 더 시간과 메모리를 아끼는 코드
# queue를 이용하지않았고 개수만 세면 되니까
# 배열에서 pop을 함
# read = stdin.readline 을 이용하여
# 인풋을 받아올 때
# read() 를 썼다.
# 또한 graph를 dic와 set 형식으로 만들어 구현했다.

#
# from sys import stdin
#
# read = stdin.readline
# v = int(read())
# e = int(read())
# graph = {}
#
# for i in range(v+1):
#   graph[i] = set()
#
# for _ in range(e):
#   a, b = map(int,read().split())
#   graph[a].add(b)
#   graph[b].add(a)
#
# visited=[1]
# queue=[1]
# while queue:
#   visit = queue.pop()
#   for i in graph[visit]:
#     if i not in visited:
#       queue.append(i)
#       visited.append(i)
#
# print(len(visited) - 1)
