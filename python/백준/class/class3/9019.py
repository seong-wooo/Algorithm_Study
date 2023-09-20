import sys
from collections import deque


def L(a):
    return (a % 1000) * 10 + a//1000


def R(a):
    return (a % 10) * 1000 + a // 10


def D(a):
    return a * 2 % 10000


def S(a):
    return a - 1 if a != 0 else 9999


input = sys.stdin.readline

q = deque()
for i in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, "L"))
    visited = [""] * 10000

    while not visited[b]:
        a, route = q.popleft()

        if not visited[a]:
            visited[a] = route
            q.append((L(a), route + "L"))
            q.append((R(a), route + "R"))
            q.append((S(a), route + "S"))
            q.append((D(a), route + "D"))

    print(visited[b][1:])
