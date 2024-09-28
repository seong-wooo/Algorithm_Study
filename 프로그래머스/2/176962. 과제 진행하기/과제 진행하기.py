from collections import deque

def solution(plans):
    plans = list(sorted(map(change_time, plans), key=lambda x:x[1]))
    plans += [['', plans[-1][1] + plans[-1][2], 0]]
    
    answer = []
    stack = deque()
    for i in range(len(plans)-1):
        time = min(plans[i+1][1] - plans[i][1], plans[i][2])
        plans[i][2] -= time
        
        if plans[i][2] > 0:
            stack.append([plans[i][0], plans[i][2]])
        else:
            answer.append(plans[i][0])            
            rest = plans[i+1][1] - plans[i][1] - time
            
            while rest > 0 and stack:
                if stack[-1][1] > rest:
                    stack[-1][1] -= rest
                    break
                name, t = stack.pop()
                rest -= t
                answer.append(name)
    
    return answer + list(map(lambda x: x[0], stack))[::-1]
            

def change_time(plan):
    h, m = map(int, plan[1].split(":"))
    
    return [plan[0], h*60+m, int(plan[2])]
    