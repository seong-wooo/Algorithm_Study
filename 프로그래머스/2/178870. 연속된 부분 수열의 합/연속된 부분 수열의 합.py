def solution(sequence, k):
    answer = []
    
    i = 0
    j = 0
    
    current = sequence[i]
    
    while i <= j and j < len(sequence):
        if current > k:
            current -= sequence[i]
            i += 1 
            
        elif current < k:
            j += 1
            if j < len(sequence):
                current += sequence[j]
            
        else:
            if not answer or answer[1] - answer[0] > j - i:
                answer = [i, j]
                
            current -= sequence[i]
            i += 1

        
    
    return answer