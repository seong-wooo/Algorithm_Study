from collections import defaultdict
import math

def solution(fees, records):
    times = defaultdict(int)
    park = dict()
    
    for record in records:
        time, num, command = record.split()
        minute = change_time(time)    
        
        if command == "IN":
            park[num] = minute
        
        else:
            in_time = park[num]
            times[num] += minute - in_time
            del park[num]
        
    max_time = change_time("23:59")
    for car in park:
        times[car] += max_time - park[car]
    
    return [fees[1] + math.ceil(max(0, (times[car] - fees[0])) / fees[2]) * fees[3]  for car in sorted(times.keys())]
        
        
        

def change_time(time):
    h, m = map(int, time.split(":"))
    return 60 * h + m