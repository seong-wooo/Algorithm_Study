import math

def solution(k, d):
    d2 = d*d
    answer = 0
    for x in range(0, d+1, k):
        y = int(math.sqrt(d2 -x*x))
        answer += y // k + 1
    return answer
        
    