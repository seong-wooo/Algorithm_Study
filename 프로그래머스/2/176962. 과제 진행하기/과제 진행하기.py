from collections import deque

def solution(plans):
    plans = deque(sorted(map(change_time, plans), key = lambda x : (x[1], x[2])))
    rest = deque()
    result = []
    
    current = [plans[0][1], plans[0][2]]
    

    while plans:
        plan = plans.popleft()
        # 현재 시각과의 차이를 구해서
        d = difference(current[0], current[1], plan[1], plan[2])
        
        # 현재, 시작 시각이 안되었다면
        if d > 0:
            # rest 에서 시간을 보낸다
            while d > 0 and rest:
                if rest[0][3] > d:
                    rest[0][3] -= d
                    break
                else:
                    d -= rest[0][3]
                    result.append(rest.popleft()[0])
            

        # 시작 시각이 되었다면
        current = [plan[1], plan[2]]
        # 다음 시작 시각과 비교하여
        if plans:
            next_plan = plans[0]
            d = difference(plan[1], plan[2], next_plan[1], next_plan[2])

            # 끝낼 수 있으면 끝내고 시각을 옮긴다.
            
            if d >= plan[3]:
                current = add_time(current[0], current[1], plan[3])
                result.append(plan[0])

            # 못 끝낸다면 rest 에 넣는다.
            else:
                current = add_time(current[0], current[1], d)
                rest.appendleft([plan[0], plan[1], plan[2], plan[3] - d])


        # 다음 시작이 없으면 그냥 결과에 넣는다.
        else:
            result.append(plan[0])
    
    for r in rest:
        result.append(r[0])
    
    return result
            
            
def change_time(plan):
    h, m = map(int, plan[1].split(":"))
    return [plan[0], h, m, int(plan[2])]


def difference(h1, m1, h2, m2):
    return (h2 - h1) * 60 + m2 - m1

def add_time(h1, m1, minute):
    new_m = m1 + minute
    
    return [h1 + new_m // 60, new_m % 60]