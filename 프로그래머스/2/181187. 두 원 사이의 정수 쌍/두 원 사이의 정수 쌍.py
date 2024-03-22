import math

def solution(r1, r2):
    answer = 0
    r12 = r1 ** 2
    r22 = r2 ** 2

    for x in range(1, r1):
        x2 = x ** 2
        r1_max = math.sqrt(r12 - x2)
        r1_max = r1_max - 1 if r1_max % 1 == 0 else int(r1_max)
        answer += int(math.sqrt(r22 - x2)) - r1_max
    
    for x in range(r1, r2):
        answer += int(math.sqrt(r22 - x ** 2))
    
    answer *= 4
    return answer + (r2 - r1 + 1) * 4