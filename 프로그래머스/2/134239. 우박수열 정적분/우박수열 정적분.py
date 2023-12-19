def solution(k, ranges):
    a = [k]
    
    while k > 1:
        k = k // 2 if k % 2 == 0 else 3 * k + 1
        a.append(k)
    
    
    area = [0]
    
    for i in range(len(a) - 1):        
        area.append(area[-1] + (a[i] + a[i + 1]) / 2)
    
    n = len(area) - 1
    
    answer = []
    for r in ranges:
        left = r[0]
        right = n + r[1]
        
        if left > right: 
            answer.append(-1)
            continue
        answer.append(area[right] - area[left])
    
    return answer