from collections import defaultdict

def solution(topping):
    chul = defaultdict(int)
    bro = defaultdict(int)
    
    for t in topping:
        bro[t] += 1
        
    answer =0  
    for i in range(len(topping) - 1):
        chul[topping[i]] += 1
        bro[topping[i]] -= 1
        if bro[topping[i]] == 0:
            del bro[topping[i]]
        
        if len(chul) == len(bro):
            answer += 1
    return answer
        
    
    
    