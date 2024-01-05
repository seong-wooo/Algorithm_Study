def solution(land):
    for j in range(len(land) - 2, -1 , -1):
        for i in range(len(land[j])):
            land[j][i] += max(land[j+1][:i] + land[j+1][i+1:])
    
    
    return max(land[0])
            
            
            
