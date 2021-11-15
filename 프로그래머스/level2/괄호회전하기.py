from collections import deque


def solution(s):
    s = deque(s)
    o = {"(", "{", "["}
    result = 0
    for i in range(len(s)):
        stack = deque()
        if i:
            s.append(s.popleft())
        for j in range(len(s)):
            if s[j] in o:
                stack.append(s[j])
            else:
                if s[j] == ")" and stack[-1:] == ['(']:
                    stack.pop()
                elif s[j] == "}" and stack[-1:] == ['{']:
                    stack.pop()
                elif s[j] == "]" and stack[-1:] == ['[']:
                    stack.pop()
                else:
                    stack.append(s[j])
                    break
        if len(stack) == 0:
            result += 1
    return result

print(solution("[](){}"))