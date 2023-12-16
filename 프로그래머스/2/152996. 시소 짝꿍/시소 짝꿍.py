from collections import Counter

def solution(weights):
    
    d = Counter(weights)
    
    answer = 0
    for key in d.keys():
        answer += d[key] * (d[key] - 1) // 2
        if key * 3 / 2 in d:
            answer += d[key] * d[key * 3 / 2]
        
        if key * 2 in d:
            answer += d[key] * d[key * 2]
        
        if key * 4 / 3 in d:
            answer += d[key] * d[key * 4 / 3]
    
    return answer
        
        
        
        
    
    return answer