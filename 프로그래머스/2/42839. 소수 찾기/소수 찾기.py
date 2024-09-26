from itertools import permutations

def solution(numbers):
    maximum = int(''.join(sorted(map(str, list(numbers)), reverse=True)))
    
    sosu = [False, False] + [True] * (maximum - 1)

    for i in range(2, int(maximum**0.5)+1):
        if sosu[i]:
            sosu[i*2:maximum + 1:i] = [False] * ((maximum - 2*i) // i + 1)
    
    
    s = set()
    for j in range(1, len(numbers) + 1):
        s.update(map(lambda x : int(''.join(x)), permutations(list(numbers), j)))
        

    return sum(sosu[i] for i in s)