def solution(n, times):
    min_time = min(times)
    end = n * min_time
    start = 0 
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        people = 0
        
        for time in times:
            people += mid // time
        
        if people >= n:
            answer = mid
            end = mid - 1
        
        else:
            start = mid + 1
    
    return answer
        