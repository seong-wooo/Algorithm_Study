from collections import deque, defaultdict
def solution(s):
    change = {
        "(": "0",
        ")": "1",
        "{": "2",
        "}": "3",
        "[": "4",
        "]": "5"
    }
    s = "".join(map(lambda x: change[x], s))
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += do(s)
    return answer


def do(s):
    d = defaultdict(deque)
    
    for i in range(len(s)):
        c = s[i]
        
        if c in "135":
            target = str(int(c) - 1)
            if not d[target]:
                return 0
            
            for o in "024":
                if target != o and d[o] and d[o][-1] > d[target][-1]:
                    return 0
                
            d[target].pop()
        else:
            d[c].append(i)

    for q in d.values():
        if q:
            return 0
    
    return 1