from collections import deque
def solution(priorities, location):
    
    
    s_p = deque(sorted(priorities, reverse=True))
    
    
    priorities = list(enumerate(priorities))

    answer = 0
    while True:
        for i in range(len(priorities)):
            if priorities[i][1] == s_p[0]:
                s_p.popleft()
                answer += 1
                if priorities[i][0] == location:
                    return answer
