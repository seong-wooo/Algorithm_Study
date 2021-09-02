# 스택의 기본 성질을 이용한 문제
# 문제를 보고 스택을 떠올렸다면 쉽게 풀 수 있는 문제였다.

import sys

k = int(sys.stdin.readline())
write_money = []
for i in range(k):
    money = int(sys.stdin.readline())
    if money == 0:
        write_money.pop()
    else:
        write_money.append(money)

print(sum(write_money))