# 나는 stack을 생각하여 맨 위를 확인하는 작업을 진행했다.
# 이때 빈 스택을 처리하기 싫어서 -1을 먼저 넣었는데
from collections import deque
def solution(arr):
    stack = deque([-1])

    for n in arr:
        if stack[-1] != n:
            stack.append(n)

    return list(stack)[1:]


# 이런 식으로 [-1:] 슬라이싱을 사용하면 빈 배열을 체크하지 않아도된다..ㄴ
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

