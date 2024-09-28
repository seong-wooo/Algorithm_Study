from math import ceil

def solution(picks, minerals):
    d = {"diamond": 25, "iron": 5, "stone": 1}
    minerals = list(map(lambda x: d[x], minerals))
    score_minerals = sorted(list(enumerate([sum(minerals[i:i+5]) for i in range(0, len(minerals), 5)]))[:sum(picks)], reverse =True, key=lambda x: x[1])
    
    answer = 0
    m = 0 
    for i in range(len(picks)):
        for j in range(picks[i]):
            index = score_minerals[m][0] * 5

            for k in range(index, min(index+5, len(minerals))):
                answer += ceil(minerals[k] / (5**(2-i)))
                
            m += 1
            
            if m == len(score_minerals):
                return answer
    return answer