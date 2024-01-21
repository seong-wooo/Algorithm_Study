def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    lr = lost & reserve
    lost -= lr
    reserve -= lr
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    r_index = 0
    answer = n - len(lost)
    
    for l in lost:
        while r_index < len(reserve) and reserve[r_index] < l - 1:
            r_index += 1
            
        if r_index == len(reserve):
            break
            
        if l - 1 <= reserve[r_index] <= l + 1:
            answer += 1
            r_index += 1
    return answer
            
            