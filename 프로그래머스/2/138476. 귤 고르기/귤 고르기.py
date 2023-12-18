from collections import Counter

def solution(k, tangerine):
    tangerine = [0] + list(sorted(Counter(tangerine).values()))

    for i in range(1, len(tangerine)):
        tangerine[i] += tangerine[i - 1]
        

    minimum = 100000
    
    left = 0
    right = 1


    while left <= right and right < len(tangerine):
        total = tangerine[right] - tangerine[left] 
        
        if total == k:
            minimum = min(right - left, minimum)
            left += 1
            right += 1
            
        elif total > k:
            minimum = min(right - left, minimum)
            left += 1
        
        else:
            right += 1
    
    
    return minimum