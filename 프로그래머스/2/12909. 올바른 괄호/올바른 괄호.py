def solution(s):
    x = 0
    
    for c in s:
        if c == "(":
            x += 1
            continue
            
        elif x == 0:
            return False
        x -= 1
    return x == 0
    