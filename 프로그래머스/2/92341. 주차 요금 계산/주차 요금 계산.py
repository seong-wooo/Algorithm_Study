from collections import defaultdict
import math
def solution(fees, records):
    r = defaultdict(list)
    
    for record in records:
        re = record.split(" ")
        h, m = re[0].split(":")
        time = int(h) * 60 + int(m)
        r[int(re[1])].append(time)
    
    answer = []
    for key in sorted(r.keys()):
        times = r[key]
        if len(times) % 2 == 1:
            times += [23 * 60 + 59]
        
        time = 0
        for i in range(0, len(times), 2):
            time += times[i+1] - times[i]
            
        time -= fees[0]
        result = fees[1]
        
        if time > 0:
            result += math.ceil(time/fees[2]) * fees[3]
        
        answer.append(result)
    return answer
        
        
        
        
        
        
        