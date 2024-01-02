from collections import defaultdict, deque
import sys

def solution(p):
    sys.setrecursionlimit(10**6)
    
    return do(p)
    
    

def do(p):
    if not p:
        return p
    
    d = defaultdict(int)
    
    index = 0
    while d["("] == 0 or d["("] != d[")"]:
        d[p[index]] += 1
        index += 1
    
    u, v = p[:index], p[index:]

    if is_correct(u):
        return u  + do(v)
    return "(" + do(v) + ")" + u[1:-1].replace("(", "[").replace(")", "(").replace("[", ")")
        

        
        
def is_correct(u):
    stack = 0
    
    for s in u:
        if s == "(":
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1
    
    if stack > 0:
        return False
    return True