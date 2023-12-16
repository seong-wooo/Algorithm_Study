from collections import defaultdict

def solution(weights):
    
    d = defaultdict(int)
    
    for weight in sorted(weights):
        d[weight] += 1
    
    # (2, 2)
    # (3, 2)
    # (4, 2)
    # (4, 3)
    
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