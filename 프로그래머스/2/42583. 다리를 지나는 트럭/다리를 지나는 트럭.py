from collections import deque

def solution(bridge, weight, trucks):
    q = deque()
    w = 0
    time = 1
    
    for truck in trucks:
        while q and time - q[0][1] >= bridge or w + truck > weight:
            f_truck, f_t = q.popleft()
            w -= f_truck
            time = f_t + bridge
        q.append((truck, time))
        w += truck
        time += 1

    return q[-1][1] + bridge

        