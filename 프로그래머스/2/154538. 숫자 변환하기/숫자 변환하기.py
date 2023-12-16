def solution(x, y, n):
    inf = 1e9
    answer = [inf] * (y + 1)
    
    answer[x] = 0
    
    for k in range(x+1, y+1):
        minimum = inf
        
        if k >= n and answer[k - n] != inf:
            minimum = min(minimum, answer[k - n] + 1)
        
        if (k / 2) % 1 == 0 and answer[k // 2] != inf:
            minimum = min(minimum, answer[k // 2] + 1)
        
        if (k / 3) % 1 == 0 and answer[k // 3] != inf:
            minimum = min(minimum, answer[k // 3] + 1)
            
        answer[k] = minimum
        
    return answer[y] if answer[y] != inf else -1
        
        