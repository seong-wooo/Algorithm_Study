from collections import deque

def solution(bridge, weight, trucks):
    q = deque()
    clock = 1
    q.append([trucks[0], clock])
    clock += 1
    current_weight = trucks[0]
    index = 1
    
    while index < len(trucks):
        if q and clock - q[0][1] > bridge:
            current_weight -= q.popleft()[0]
            
        if current_weight + trucks[index] <= weight:
            q.append([trucks[index], clock])
            current_weight += trucks[index]
            clock += 1
            index += 1
            
        else:
            t, c = q.popleft()
            current_weight -= t
            clock = c + bridge

            
    return q[-1][1] + bridge