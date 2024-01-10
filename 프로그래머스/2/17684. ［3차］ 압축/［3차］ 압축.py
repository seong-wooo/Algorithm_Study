def solution(msg):
    d = {chr(a): a - 64 for a in range(65, 91)}
    left = 0
    next_index = 27
    answer = []
    while left < len(msg):
        right = left + 1 # right : 포함되지 않은 index
        while right <= len(msg) and msg[left:right] in d:
            right += 1
    
        if right == len(msg) + 1:
            answer.append(d[msg[left:]])
            return answer
             
        d[msg[left:right]] = next_index
        next_index += 1
        answer.append(d[msg[left:right-1]])
        left = right - 1
        
    return answer  
        
        
        
        