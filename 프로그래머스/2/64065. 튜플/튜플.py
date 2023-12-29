def solution(s):
    s = list(map(lambda x :  list(map(int, x.split(","))), s.replace("{{", "").replace("}}", "").split("},{")))
    
    s.sort(key = lambda x : len(x))
    
    result = set(s[0])
    answer = s[0]
    
    for p in s:
        add = set(p) - result
        result.update(add)
        for a in add:
            answer.append(a)
    
    return answer