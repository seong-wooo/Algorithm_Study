from collections import deque
from heapq import heappop, heappush

def solution(jobs):
    jobs.sort(key = lambda x : (x[0], x[1]))
    q = [ [jobs[0][1], jobs[0][0]] ] 
    index = 1
    current_time = jobs[0][0]
    answer = 0
    
    while q:
        duration, req_time = heappop(q)
        current_time += duration
        answer += current_time - req_time
        
        while index < len(jobs) and jobs[index][0] <= current_time:
            heappush(q, [jobs[index][1], jobs[index][0]])
            index += 1
        
        if not q and index < len(jobs):
            heappush(q, [jobs[index][1], jobs[index][0]])
            current_time = jobs[index][0]
            index += 1
        
    return answer // len(jobs)
            
            
    
        
        

        