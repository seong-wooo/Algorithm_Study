from collections import deque
def solution(s):
    change = {
        "(": "0",
        ")": "1",
        "{": "2",
        "}": "3",
        "[": "4",
        "]": "5"
    }
    s = "".join(map(lambda x: change[x], s))
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += do(s)
    return answer


def do(s):
    q = deque()
    
    for i in range(len(s)):
        c = s[i]
        
        if c in "135":
            target = str(int(c) - 1)
            if not q or q[-1] != target:
                return 0
            q.pop()
        else:
            q.append(c)
    
    return 1 if not q else 0