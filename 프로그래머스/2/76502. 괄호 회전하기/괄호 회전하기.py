# 회전을 통해 s를 올바른 문자열로 만든다
# s안에 올바른 문자열이 몇 개 있는지 확인한다

from collections import deque
def solution(s):
    
    for _ in range(len(s)):
        if not is_right(s):
            s = s[1:] + s[0]

    if not is_right(s):
        return 0
    
    print(s)
    left = 0
    right = 1
    answer = 0
    
    while right < len(s):
        if is_right(s[left:right+1]):
            answer += 1
            left = right + 1
            right = left + 1
            continue
        
        right += 1
    
    return answer
    
            
        
        

def is_right(s):
    q = deque()
    
    for c in s:
        if not q:
            if c == ")" or c == "}" or c == "]":
                return False
            q.append(c)
            continue
        
        if c == ")" and q[-1] == "(":
            q.pop()
        elif c == "}" and q[-1] == "{":
            q.pop()
        elif c == "]" and q[-1] == "[":
            q.pop()
        else:
            q.append(c)
    
    return not q
        
        
        
        
            
        
