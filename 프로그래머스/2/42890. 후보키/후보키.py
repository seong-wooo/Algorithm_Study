from itertools import combinations

def solution(relation):
    
    answer = set()
    index = [i for i in range(len(relation[0]))]
    
    
    for count in range(1, len(relation) + 1):
        for c in combinations(index, count):
            if isIn(answer, c):
                continue
                    
            
            
            s = set()
            for j in range(len(relation)):
                s.add(tuple(relation[j][k] for k in c))
            
            
            if len(s) == len(relation):
                answer.add(c)

    return len(answer)
            
                    
def isIn(answer, c):
    c = set(c)
    for a in answer:
        a = set(a)
        if a & c == a:
            return True
    return False