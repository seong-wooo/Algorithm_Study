# 그리디로 풀어본다.
# 정렬을 먼저 한다.
# 앞에서 부터 범위에 포함되면 리스트 재조정
# 범위에 포함되지 않으면 삽입

def solution(targets):
    
    targets.sort(key = lambda x: (x[0], x[1]))
    
    shoot = [targets[0]]
    
    print(shoot)
    for target in targets[1:]:
        if shoot[-1][1] > target[0]:
            shoot[-1] = [target[0], min(shoot[-1][1], target[1])]
        else:
            shoot.append(target)
    
    return len(shoot)
    
    