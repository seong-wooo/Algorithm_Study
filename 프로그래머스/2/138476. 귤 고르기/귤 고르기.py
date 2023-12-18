from collections import Counter

def solution(k, tangerine):
    answer = 0
    for t in sorted(Counter(tangerine).values(), reverse = True):
        k -= t
        answer += 1
        if k <= 0:
            return answer
    return -1

    