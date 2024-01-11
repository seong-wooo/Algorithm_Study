def solution(number, limit, power):
    answer = 0 
    for i in range(1, number + 1):
        count = divisor(i)
        if count > limit:
            answer += power
        else:
            answer += count
            
    return answer
            

def divisor(n):
    s = set()
    for i in range(1, int(n ** 0.5)+ 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return len(s)
        