from collections import defaultdict

def solution(topping):
    left_counter = defaultdict(int)
    right_counter = defaultdict(int)
    
    left_counter[topping[0]] += 1
    for i in range(1, len(topping)):
        right_counter[topping[i]] += 1
    

    answer = 0
    for i in range(1, len(topping)):
        if len(left_counter) == len(right_counter):
            answer += 1
        
        left_counter[topping[i]] += 1
        right_counter[topping[i]] -= 1
        if right_counter[topping[i]] == 0:
            del right_counter[topping[i]]
        
    return answer