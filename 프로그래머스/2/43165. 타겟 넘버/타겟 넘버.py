from collections import deque

def solution(numbers, target):
    q = deque()
    q.append((-1, 0))
    answer =0
    while q:
        index, result = q.popleft()
        
        if index == len(numbers) - 1:
            if result == target:
                answer += 1
            continue
            
        next_index = index + 1
        next_num = numbers[next_index]
        q.append((next_index, result+next_num))
        q.append((next_index, result-next_num))
    return answer       
            
                
        
    
    
    
    