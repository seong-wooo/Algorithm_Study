# 처음에는 L,D,P,B 입력을 받을 때 마다 명령을 수행했다.
# B나 P를 실행할 때 리스트 중간에 데이터를 추가하거나 삭제할 때
# 시간이 오래걸린다.
# 따라서 큐나 스택을 만들어서
# 커서의 바로 앞이 큐나 스택의 맨 위에 위치하도록 만들었다.
# 리스트로 구현한 스택이 더 시간이 짧게 걸린다.

# 큐를 두 개 사용하는 방식
import sys
from collections import deque

input = sys.stdin.readline
string = deque(input().rstrip())

queue = deque()

for _ in range(int(input())):
    commend, *x = input().split()

    if commend == "L":
        if string:
            queue.appendleft(string.pop())

    elif commend == "D":
        if queue:
            string.append(queue.popleft())

    elif commend == "B":
        if string:
            string.pop()

    else:
        string.append(x[0])

print("".join(string) + "".join(queue))


# 스택을 두 개 사용하는 방식
import sys

input = sys.stdin.readline
string_l = list(input().rstrip())

string_r = list()

for _ in range(int(input())):
    commend, *x = input().split()

    if commend == "L":
        if string_l:
            string_r.append(string_l.pop())

    elif commend == "D":
        if string_r:
            string_l.append(string_r.pop())

    elif commend == "B":
        if string_l:
            string_l.pop()

    else:
        string_l.append(x[0])

print("".join(string_l + string_r[::-1]))