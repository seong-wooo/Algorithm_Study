def solution(A, B):
    A.sort()
    B.sort()
    
    i = 0
    result = 0
    
    for j in range(len(B)):
        if B[j] > A[i]:
            i += 1
            result += 1
    return result
            
        
        
    