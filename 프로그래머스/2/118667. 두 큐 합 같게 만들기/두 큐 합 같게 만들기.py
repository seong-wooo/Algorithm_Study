def solution(queue1, queue2):
    q1 = sum(queue1)
    q2 = sum(queue2)
    
    total = q1 + q2
    if total % 2 != 0:
        return -1
    
    target = total // 2
    
    q = queue1 + queue2
    start = 0
    end = len(queue1) - 1
    answer = 0
    
    while q1 != target and start <= end:
        if q1 < target:
            end += 1
            if end == len(q)-1:
                return -1
            q1 += q[end]
        else:
            q1 -= q[start]
            start += 1
        answer += 1
    return answer 
        
            