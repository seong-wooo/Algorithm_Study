from collections import Counter, deque

def solution(p, l):
    counter = [0] * 10
    
    for num in p:
        for i in range(1, num):
            counter[i] += 1
    
    p = deque(zip(p,[i for i in range(len(p))]))
    answer = 1
    while True:
        if counter[p[0][0]] == 0:
            t = p.popleft()
            if t[1] == l:
                return answer
            for i in range(1, t[0]):
                counter[i] -= 1
            answer += 1
            
        else:
            p.append(p.popleft())
            
        
            
    return answer        
        
    