from itertools import combinations

def solution(relation):
    column = [j for j in range(len(relation[0]))]
    answer = set()
    
    for i in range(1, len(relation[0]) + 1):
        for comb in combinations(column, i):
            if not issuperset(comb, answer) and isprimarykey(relation, comb):
                answer.add(tuple(comb))
                
    return len(answer)
                
                

def issuperset(comb, answer):
    for a in answer:
        if set(a).issubset(set(comb)):
            return True
    return False
                    
                    
def isprimarykey(relation, comb):
    keys = set()
    for row in relation:
        t = [row[i] for i in comb]
        for key in keys:
            if list(key) == t:
                return False
            
        keys.add(tuple(t))
    return True
                

