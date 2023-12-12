# 투 포인터 방식으로 푼다.

from collections import defaultdict

def solution(sequence, k):    
    d = defaultdict(list)
    
    left = 0
    right = 0
    current = sequence[left]
    
    while left <= right and right < len(sequence):
        
        if current == k:
            if not d[right - left]:
                d[right - left] = [left, right]
            
            current -= sequence[left]
            left += 1
            right += 1
            if right < len(sequence):
                current += sequence[right]
        
        elif current > k:
            current -= sequence[left]
            left += 1
        
        else:
            right += 1
            if right < len(sequence):
                current += sequence[right]
                

    return d[min(d.keys())]
        
