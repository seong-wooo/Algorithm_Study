def solution(sequence, k):
    answer = []
    length = len(sequence)
    
    left = 0
    right = 0
    current = sequence[0]
    
    while right < len(sequence):
        if current == k:
            if length > right - left:
                answer = [left, right]
                length = right - left
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
    
    return answer
        