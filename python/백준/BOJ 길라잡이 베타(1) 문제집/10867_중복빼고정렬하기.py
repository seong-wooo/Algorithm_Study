#굉장히 쉬운문제
# 음수의 값이 들어갈 수 있으니까
# map을 이용하여 int로 바꿔서 정렬을 한다.

n = input()
arr = list(set(map(int,input().split())))
arr.sort()
for i in arr:
  print(i, end = " ")