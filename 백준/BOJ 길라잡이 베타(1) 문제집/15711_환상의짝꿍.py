# 골드바흐의 추측을 이용
# 4보다 큰 짝수는 두 소수의 합으로 표현 가능
# 2*(10**12)는 너무 큰 수이므로
# 루트를 씌운값을 통해 알고리즘 진행함

import sys
n = 2*(10**6)
primes = [False,False] + [True] * (n-1)
for i in range(3,int(n**0.5)+1,2):
    if primes:
        primes[i*2::i] = [False] * ((n-i)//i)

primes = [x for x in range(3,n+1,2) if primes[x]]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    c = a + b
    if c % 2 == 0 and c >= 4:
        print("YES")
    else:
        c -= 2
        for i in primes:
            if i**2 > c:
                break
            elif c % i == 0:
                c = -1
                break

        if c <= 1:
            print("NO")
        else:
            print("YES")


