#숫자 카드 게임
#입력 받는 행에서 가장 작은 값만 골라서 a 리스트에 삽입한다
# a 리스트에서 가장 큰 값을 출력한다.
# 상당히 쉬운 문제

import sys

n, m = map(int, sys.stdin.readline().split())

a = []
for i in range(n):
  a.append(min(map(int, sys.stdin.readline().split())))

print(max(a))


