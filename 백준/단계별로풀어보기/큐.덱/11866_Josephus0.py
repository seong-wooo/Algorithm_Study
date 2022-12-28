# 원형 큐를 생각하면 쉬운 문제였지만
# 인덱스와 각 항이 1이 차이나는 것을 해결하느라 오래걸렸다.
# 처음에 k -= 1 을 진행한 상태로 하면 쉬운거였는데;..


import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, n+1)])

K = k
k -= 1
print("<",end="")
while len(deq) > 1:
    print(deq[k], end = ", ")
    del deq[k]
    k += K -1
    if len(deq) >0 and k >= len(deq):
        k %= len(deq)
print(str(deq[0])+">")




