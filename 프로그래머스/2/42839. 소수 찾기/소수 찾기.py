from itertools import permutations as per

def solution(numbers):
    m = int("".join(sorted(list(numbers), reverse = True)))    
    sosu = [False, False] + [True] * (m - 1)
    for i in range(2, int(m ** 0.5) + 1): 
        if sosu[i]:
            sosu[i*2::i] = [False] * len(sosu[i*2::i])
            
    answer = 0
    for j in range(1, len(numbers) + 1):
        for p in per(numbers, j):
            p = int("".join(p))
            if sosu[int(p)]:
                answer += 1
                sosu[int(p)] = False
    
    return answer