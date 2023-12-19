from math import gcd
def solution(arrayA, arrayB):
    gcd_a = arrayA[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
    
    gcd_b = arrayB[0]
    for i in range(1, len(arrayB)):
        gcd_b = gcd(gcd_b, arrayB[i])

    if gcd_a == gcd_b == 1:
        return 0
    
    answer = gcd_a
    for b in arrayB:
        if b % gcd_a == 0:
            answer = 0
            break
    
    if answer > gcd_b:
        return answer
    
    answer = gcd_b
    for a in arrayA:
        if a % gcd_b == 0:
            answer = 0
            break
        
    return answer