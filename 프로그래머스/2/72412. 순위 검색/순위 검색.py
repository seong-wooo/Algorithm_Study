from collections import defaultdict
from bisect import bisect_left
import re

def solution(infos, query):
    data = defaultdict(list)
    
    for info in infos:
        s_info = info.split(" ")
        
        for i in (s_info[0], "-"):
            for j in (s_info[1], "-"):
                for k in (s_info[2], "-"):
                    for l in (s_info[3], "-"):
                        data[(i,j,k,l)].append(int(s_info[4]))
    for key in data:
        data[key].sort()
    
    answer = []
    for q in query:
        s_q = re.split(" and | ", q)
        scores = data[tuple(s_q[:4])]
            
        answer.append(len(scores) - bisect_left(scores, int(s_q[4])))
    return answer