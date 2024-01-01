from itertools import permutations as per

def solution(expression):
    
    answer = 0
    for order in per("+-*", 3):
        answer = max(abs(int(calc(expression, "".join(order)))), answer)
    return answer


def calc(ex, symbols):
    if not symbols:
        return ex
    
    answer = symbols[0].join(map(lambda x : calc(x, symbols[1:]), ex.split(symbols[0])))
    return str(eval(answer))
        
