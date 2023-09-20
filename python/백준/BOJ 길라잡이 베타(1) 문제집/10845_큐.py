# 기본적인 큐를 구현
# print를 할 때 결과를 합쳐서 print 하는 연습을 하자
# 또한 if else를 간략하게 쓰는 방법을 자주 사용하자
# 밑에는 그 예시 코드이다.

from collections import deque
import sys

input = sys.stdin.readline

queue = deque()

for i in range(int(input())):
  inst = input().split()

  if inst[0] =="push":
    queue.append(inst[1])
  elif inst[0] == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif inst[0] == "pop":
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif inst[0] == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)
  elif inst[0] == "size":
    print(len(queue))
  else:
    if queue:
      print(0)
    else:
      print(1)


# 더 빠르고 간략한 코드
import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines()
for idx in range(t):
    a,*b = L[idx].split()
    if "push" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1")
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop":
        res.append(q.pop(0) if q else "-1")
print("\n".join(res))