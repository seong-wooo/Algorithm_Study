def solution(msg):
    index = 1
    d = dict()
    
    for a in range(ord('A'), ord('Z') + 1):
        d[chr(a)] = index
        index += 1
    
    answer = []
    i = 0
    while i < len(msg):
        j = i + 1
        while j <= len(msg) and msg[i:j] in d:
            j += 1    
        
        if j > len(msg):
            return answer + [d[msg[i:]]]
        
        d[msg[i:j]] = index
        index += 1
        
        answer.append(d[msg[i:j-1]])
        i = j - 1
    return answer
    