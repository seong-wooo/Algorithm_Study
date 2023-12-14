import math

def solution(picks, minerals):
    total = sum(picks) * 5
    minerals = minerals[:total if len(minerals) > total else len(minerals)]

    m = {k: v for k,v in zip(["diamond", "iron", "stone"], [25, 5, 1])}
    minerals_value = [[0] * 5 for _ in range(math.ceil(len(minerals) / 5))]
    
    for i in range(len(minerals)):
        c, l = i // 5, i % 5
        minerals_value[c][l] = m[minerals[i]]
    
    minerals_value.sort(key=lambda x: sum(x), reverse = True)
    
    result = 0
    damage = [25, 5, 1]
    for values in minerals_value:
        for j in range(3):
            if picks[j]:
                result += sum(map(lambda v: math.ceil(v / damage[j]), values))
                picks[j] -= 1
                break
            
                
        
    return result