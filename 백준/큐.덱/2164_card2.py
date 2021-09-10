# deque()를 사용하여 덱을 구현했다.
# popleft와 append를 이용하여 pop과 push를 구현했다.

import sys
from collections import deque

n = int(sys.stdin.readline())

d = deque([i for i in range(1,n+1)])


while len(d) != 1:
    d.popleft()
    d.append(d.popleft())

print(d[0])