def solution(x, y, n):
    all = set()
    all.add(x)    
    answer = 0
    
    s = set()
    s.add(x)
    
    while s:
        if y in s:
            return answer
        
        round = set()
        for num in s:
            for j in [num + n, num * 2, num * 3]:
                if j <= y and j not in all:
                    round.add(j)
                    all.add(j)
        answer += 1
        s = round
        
    return -1
        
            
            
    
    