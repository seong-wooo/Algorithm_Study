from collections import Counter


def solution(weights):
    c = Counter(weights)
    answer = 0
    for key in c:
        answer += (c[key] * (c[key] - 1)) // 2
        
        if key*2/3 in c:
            answer += c[key] * c[key*2/3]
        
        if key*2 in c:
            answer += c[key] * c[key*2]
        
        if key*3/4 in c:
            answer += c[key] * c[key*3/4]
        
    return answer