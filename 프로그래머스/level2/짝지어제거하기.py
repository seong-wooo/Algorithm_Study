# 스택을 이용
# 짝지어 제거하는 문제는 스택을 먼저 생각해보자
def solution(s):
    # 스택 한개
    stack = []
    for alpha in s:
        if stack[-1:] == [alpha]:
            stack.pop()
        else:
            stack.append(alpha)
    if stack:
        return 0
    return 1