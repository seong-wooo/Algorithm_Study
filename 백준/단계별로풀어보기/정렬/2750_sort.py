# 리스트를 이용하여 정렬한다.

a = []
for i in range(int(input())):
    a.append(int(input()))
a.sort()

for j in a:
    print(j)