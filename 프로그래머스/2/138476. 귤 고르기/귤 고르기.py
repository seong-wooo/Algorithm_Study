from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)
    k = len(tangerine) - k
    
    for num in sorted(c.keys(), key=lambda x:c[x]):
        if c[num] > k or k == 0:
            break
        k -= c[num]
        c.pop(num)
    

    return len(c)