# 축을 제외한 1사분면에서의 점 개수를 구한다.
# 구한 값 * 4 + 축의 점 * 4

# x = 1 ~ r1 - 1 일 때 .. 개수
# ---
# x = r1 ~ r2 - 1 일 때 개수

# y = sqrt(r^2 - x^2)

import math

def solution(r1, r2):
    
    answer = 0
    
    for x in range(1, r1):
        r1_max = math.sqrt(r1**2 - x**2)
        r1_max = r1_max - 1 if r1_max % 1 == 0 else int(r1_max)
            
        r2_max = int(math.sqrt(r2**2 - x**2))
        
        answer += r2_max - r1_max
    
    for x in range(r1, r2):
        answer += int(math.sqrt(r2**2 - x**2))
        
    answer *= 4
    
    answer += (r2 - r1 + 1) * 4
    
    return answer