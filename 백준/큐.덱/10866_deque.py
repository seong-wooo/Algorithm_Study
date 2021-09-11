# 기본적인 덱의 성질을 구현한 문제
# 덱의 성질 : 맨 앞이나 맨 뒤에서 pop,push기능을 사용할 수 있다.

import sys
from collections import deque

d = deque()

for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline()

    ins = s.split()[0]

    if ins == "push_front":
        d.appendleft(s.split()[1])

    elif ins == "push_back":
        d.append(s.split()[1])

    elif ins == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)

    elif ins == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)

    elif ins == "size":
        print(len(d))

    elif ins =="empty":
        if d:
            print(0)
        else:
            print(1)
    elif ins =="front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif ins =="back":
        if d:
            print(d[-1])
        else:
            print(-1)