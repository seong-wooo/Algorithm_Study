# 에라토네스의 체 이용하는 문제
# list에서 검색을 하는 경우 시간 초과가 떴음
# 그래서 primes2 =set(primes)를 만들어서 검색함
# 사실 2의 배수는 검색할 이유가 없으므로
# 3부터 2씩 증가하며 검사하는 것이 더 빠른 코드

import sys

primes = [False, False] + [True] * 999999
for i in range(2, int(1000001**0.5) + 1):
    if primes[i]:
        primes[i*2::i] = [False] *((1000000 - i) // i)
primes = [x for x in range(1000000) if primes[x]]
primes2 = set(primes)
while True:
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    i = 1
    while primes[i] < n:
        if n - primes[i] in primes2:
            print(f"{n} = {primes[i]} + {n - primes[i]}")
            break
        else:
            i += 1


