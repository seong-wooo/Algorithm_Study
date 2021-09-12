# 큐와 덱이 헷갈려서 오래걸렸다.
# 큐는 first in first out..
# 문제를 잘 읽자
# 1번보기에서 pop은 맨 왼쪽에서만 가능하다고 하였다.
# 해당 인덱스에서 맨 왼쪽과 오른쪽 중 더 가까운 곳을 향해 간다.

import sys

#크기, 뽑는 수
from collections import deque

n, m = map(int, sys.stdin.readline().split())

loc = list(map(int, sys.stdin.readline().split()))

d = deque([i for i in range(1,n+1)])

count = 0

for i in range(m):
    index = d.index(loc[i])
    if index < len(d) - index:
        for j in range(index):
            d.append(d.popleft())
            count += 1
        d.popleft()
    else:
        for k in range(len(d) - index):
            d.appendleft(d.pop())
            count += 1
        d.popleft()

print(count)





