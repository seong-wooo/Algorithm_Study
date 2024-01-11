def solution(s):
    answer = 0
    while s:
        x = s[0]
        x_count = 1
        y_count = 0
        
        for i in range(1, len(s)):
            if s[i] == x:
                x_count += 1
            else:
                y_count += 1 
            
            if x_count == y_count:
                s = s[i+1:]
                answer += 1
                break
        else:
            return answer + 1
        
    return answer
                