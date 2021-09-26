# 큰 수의 법칙

import sys


n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
# 가장 큰 수와 두 번째로 큰 수
first, second = num[-1], num[-2]

#나눗셈 연산을 많이 하지말고 + - 연산으로 대체하자
#count -> 가장 큰 수가 더해지는 횟수
#m-count -> 두 번째로 큰 수가 더해지는 횟수
count = k * (m//(k+1)) + m % (k+1)
total = first*count+ second *(m-count)
print(total)