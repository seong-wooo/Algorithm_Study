# 해시 함수( set )를 이용하여 구현하였다.
# 밑의 간략하고 더 빠른 코드를 집중적으로 보자

import sys

input = sys.stdin.readline

n = input()
n_set =set(map(int,input().split()))

m = input()
m_list = list(map(int, input().split()))

for num in m_list:
  if num in n_set:
    print(1, end = " ")
  else:
    print(0, end= " ")




# 더 간략하고 좋은 코드
# 내 코드에서 굳이 m_list를 만들 이유가 없다
# 그리고 int형으로 굳이 바꿔줄 이유가 없다

input = sys.stdin.readline
input()
a=set(input().split())
input()
print(' '.join(['1' if j in a else '0' for j in input().split()]))