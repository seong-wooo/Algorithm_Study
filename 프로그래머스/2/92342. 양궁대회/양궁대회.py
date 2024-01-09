def solution(n, info):
    return shoot(n, info, [])[1]
    

def shoot(n, apeach, lion):    
    result = [-1, [-1]]
    if n == 0 or len(apeach) == len(lion):
        lion += [0] * (len(apeach) - len(lion))
        lion[-1] += n
        
        a, l = 0, 0
        for i in range(len(lion)):
            if lion[i] > apeach[i]:
                l += 10 - i
            elif apeach[i] != 0:
                a += 10 - i

        return [l - a, lion] if l > a else result

    index = len(lion)
    if n > apeach[index]:
        result = max(result, shoot(n - apeach[index] - 1, apeach, lion + [apeach[index] + 1]), key = lambda x : (x[0], *reversed(x[1])))
    result = max(result, shoot(n, apeach, lion + [0]), key = lambda x : (x[0], *reversed(x[1])))

    return result

    