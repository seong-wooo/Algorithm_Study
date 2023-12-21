from collections import defaultdict

def solution(want, number, discount):
    w = defaultdict(int)
    for i in range(len(want)):
        w[want[i]] += number[i]
    
    
    d = defaultdict(int)
    for i in range(10):
        d[discount[i]] += 1
    
    result = contains(w, d)
    for i in range(1, len(discount) - 9):

        d[discount[i - 1]] -= 1
        d[discount[i + 9]] += 1
        if d[discount[i - 1]] == 0:
            d.pop(discount[i -1])
        result += contains(w, d)
        
    return result
        
    
def contains(w, d):
    for v in w:
        if not d[v] or w[v] > d[v]:
            return 0
    return 1