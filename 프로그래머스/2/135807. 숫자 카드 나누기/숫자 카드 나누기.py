from math import gcd

def solution(arrayA, arrayB):
    # 각각의 최대 공약수를 구한다
    
    A = arrayA[0]
    i = 1
    while i < len(arrayA):
        A = gcd(A, arrayA[i])
        i += 1
    
    B = arrayB[0]
    i = 1
    while i < len(arrayB):
        B = gcd(B, arrayB[i])
        i += 1
        
    answer = 0
    if all(b % A != 0 for b in arrayB):
        answer = max(answer, A)
            
    if all(a % B != 0 for a in arrayA):
        answer = max(answer, B)
    
    return answer