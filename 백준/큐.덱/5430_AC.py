# R -> 뒤집기/ 배열에 있는 숫자 순서 뒤집기
# D -> 버리기/ 첫 번째 숫자 버리기 (배열이 비어있지 않은경우)
# 되게 쉬운문제였는데 어디선지 모르게 에라가 났다.
# R이 나올때마다 reverse를 하는 것이 아니라 
# R_count 에 따라 마지막에 최대 1번만 reverse를 진행한다

import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().strip()

    R_count = 0
    error = False
    if n == 0:
        x = deque()
    else:
        x = deque(x[1:-1].split(","))
    for j in p:
        if j == "R":
            R_count +=1
        elif j == "D":
            if x:
                if R_count % 2 == 1:
                    x.pop()
                else:
                    x.popleft()
            else:
                error = True
                print("error")
                break
    if error == False:
        if R_count % 2 == 1:
            x.reverse()
        print("[" + ",".join(x) + "]")
