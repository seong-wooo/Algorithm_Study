# D 2배 (2n % 10000)
# S n - 1 if not n else 9999
# L d1 d2 d3 d4 -> d2 d3 d4 d1
# R d4 d1 d2 d3

import sys
from collections import deque


def D(n):
    return (2 * n) % 10000


def S(n):
    return n - 1 if n else 9999


def L(n):
    return (n % 1000) * 10 + n // 1000


def R(n):
    return (n % 10) * 1000 + n // 10


input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    visited = [""] * 10000
    q.append(a)
    visited[a] = "A"

    while q:
        now = q.popleft()

        if now == b:
            print(visited[now][1:])
            break

        next = [D(now), S(now), L(now), R(now)]
        command = ["D", "S", "L", "R"]
        for i in range(4):
            if not visited[next[i]]:
                visited[next[i]] = visited[now] + command[i]
                q.append(next[i])

