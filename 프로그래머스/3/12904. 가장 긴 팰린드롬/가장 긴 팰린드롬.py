def solution(s):
    answer = 1
    
    for i in range(len(s)-1):
        for j in range(i+answer, len(s)):
            p = s[i:j+1] 
            if p == p[::-1]:
                answer = max(answer, len(p))
    return answer