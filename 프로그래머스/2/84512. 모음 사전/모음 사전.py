from itertools import product

def solution(word):
    a = []
    for i in range(1, 6):
        a += list(map(lambda x: ''.join(x), product(['A','E','I','O','U'], repeat=i)))
    

    return sorted(a).index(word) + 1