# 큐를 이용하여 문제를 구현하였다.
# 알고자 하는 항의 위치를 계속하여 저장하고
# 항의 위치가 0일때 프린트를 할 조건이 만족되면
# 프린트를 하고 아니면 다시 맨 뒤로 보낸다.



import sys

from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    #문서 개수, 큐 순서
    n, m = map(int, sys.stdin.readline().split())
    imp = deque(list(map(int, sys.stdin.readline().split())))

    count = 0
    loc = m
    while True:
        if loc > 0:
            if imp[0] == max(imp):
                imp.popleft()
                count += 1
                loc -= 1
            else:
                imp.append(imp.popleft())
                loc -= 1

        elif loc == 0:
            if len(imp) == 1:
                count += 1
                print(count)
                break
            elif imp[0] >= max(imp):
                count+=1
                print(count)
                break
            else:
                imp.append(imp.popleft())
                loc = len(imp) - 1



