from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    change = {
        "cpp": "0",
        "java": "1",
        "python": "2",
        "backend" : "0",
        "frontend" : "1", 
        "junior" : "0",
        "senior" : "1",
        "chicken" : "0",
        "pizza" : "1"
    }
    
    d = defaultdict(list)
    
    for inf in info:
        s = inf.split(" ")
        d["".join(map(lambda x : change[x], s[:4]))].append(int(s[4]))
    
    for key in d:
        d[key].sort()
    
    query = [q.replace(" and ", " ").split(" ") for q in query]
    answer = []
    for q in query:
        key = "".join(map(lambda x: change[x] if x in change else x, q[:4]))
        value = int(q[4])
        
        keys = find_keys(key, "")
        result = 0
        for key in keys:
            if key in d:
                result += len(d[key]) - bisect_left(d[key], value)
                
        answer.append(result)
    return answer
            
            

def find_keys(key, k):
    if len(key) == len(k):
        return [k]
    
    keys = []
    next = len(k)
    if key[next] == "-":
        keys += find_keys(key, k + "0")
        keys += find_keys(key, k + "1")
        keys += find_keys(key, k + "2")
        
    else:
        keys += find_keys(key, k + key[next])
    
    return keys