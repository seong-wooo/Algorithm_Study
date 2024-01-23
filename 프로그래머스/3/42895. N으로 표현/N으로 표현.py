from collections import defaultdict

def solution(N, number):    
    d = defaultdict(set)      
    
    n_s = str(N)
    # N을 사용한 횟수
    for i in range(1, 9):
        d[i].add(int(n_s * i))
        for j in range(1, i):
            for n1 in d[i - j]:
                for n2 in d[j]:
                    d[i].add(n1 + n2)
                    d[i].add(n1 - n2)
                    d[i].add(n1 * n2)
                    if n1 != 0 and n2 != 0:
                        d[i].add(n1 // n2)
                        d[i].add(n2 // n1)
        
        if number in d[i]:
            return i
    
    return -1
            
    