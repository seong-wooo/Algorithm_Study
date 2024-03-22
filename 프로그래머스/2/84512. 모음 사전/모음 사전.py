from itertools import product

def solution(word):
    result = []
    for i in range(1, 6):
        for p in product("AEIOU", repeat = i):
            result.append("".join(p))
    
    result.sort()
    
    return result.index(word) + 1
