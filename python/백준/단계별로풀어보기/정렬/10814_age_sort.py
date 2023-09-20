# 먼저 가입한 순서대로 정렬하는 부분이 헷갈렸었는데
# 이는 그냥 age 리스트 안에 있던 순서이므로
# 따로 코드를 추가할 필요가 없다

import sys

n = int(sys.stdin.readline())

age = []
for i in range(n):
    age.append(list(sys.stdin.readline().split()))

age.sort(key=lambda x: int(x[0]))

for j in age:
    print(j[0], j[1])