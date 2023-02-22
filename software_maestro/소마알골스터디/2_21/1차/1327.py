import sys
from collections import deque


def to_str(s):
    return "".join(map(str, s))


def reverse(s, index, k):
    # index 부터 오른쪽 k개의 위치를 변경한다.
    new_s = s[::]
    new_s[index:index + k] = reversed(new_s[index:index + k])

    return new_s

input = sys.stdin.readline

n, k = map(int, input().split())

s = list(map(int, input().split()))

answer = sorted(s)
visited = dict()
q = deque()
q.append(s)
visited[to_str(s)] = 0

while q:
    s = q.popleft()

    if s == answer:
        print(visited[to_str(s)])
        break

    for i in range(n + 1 - k):
        r = reverse(s, i, k)
        tostr = to_str(r)
        if tostr not in visited:
            visited[tostr] = visited[to_str(s)] + 1
            q.append(r)



if s != answer:
    print("-1")