# 나의 풀이 평소 풀던대로
def solution(n):
    primes = [False,False] + [True] * (n-1)
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            primes[i+i::i] = [False] * ((n-i)//i)
    return primes.count(True)


# 에라토네스의 체 다른 버전
# set()으로 구현
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)