from itertools import permutations

def solution(k, dungeons):

    answer = 0
    for per in permutations(dungeons, len(dungeons)):
        result = 0
        piro = k
        for min_piro, somo_piro in per:
            if piro >= min_piro:
                result += 1
                piro -= somo_piro
        answer = max(answer, result)
              
    return answer