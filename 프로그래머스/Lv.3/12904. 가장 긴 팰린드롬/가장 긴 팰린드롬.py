def solution(s):
    answer = 1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            target = s[i:j+1]
            
            if target == target[::-1]:
                answer = max(answer, j - i + 1)
                
    return answer