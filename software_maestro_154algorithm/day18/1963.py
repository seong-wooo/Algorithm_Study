import sys
from collections import deque
sys.setrecursionlimit(10**6)


input = sys.stdin.readline

sosu = [False, False] + [True] * 9998

for i in range(2, int(len(sosu) ** 0.5) + 1):
    if sosu[i]:
        sosu[i * 2::i] = map(lambda x: False, sosu[i * 2::i])

for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append(a)

    visited = [0] * 10000
    visited[a] = 1
    while q:
        now = q.popleft()

        if now == b:
            print(visited[now] - 1)
            break

        # 1000 단위 바꾸기
        for i in range(1000, 10000, 1000):
            next = now % 1000 + i
            if sosu[next] and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

        # 100 단위 바꾸기
        for i in range(0, 1000, 100):
            next = now // 1000 * 1000 + i + now % 100
            if sosu[next] and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

        # 10 단위 바꾸기
        for i in range(0, 100, 10):
            next = now // 100 * 100 + i + now % 10
            if sosu[next] and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

        # 1 단위 바꾸기
        for i in range(0, 10):
            next = now // 10 * 10 + i
            if sosu[next] and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
