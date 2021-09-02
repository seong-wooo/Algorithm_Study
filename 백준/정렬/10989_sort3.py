# b라는 리스트를 만들고 중복된 숫자가 나오면
# 숫자 인덱스에 해당하는 값을 1 증가시킨다
# 중복되지 않게 리스트에 넣고
# 리스트를 정렬 후 중복된 숫자만큼 출력한다.

import sys

a = []
b = [0 for _ in range(10001)]

for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if b[x] > 0:
        b[x] += 1
        continue
    else:
        b[x] = 1
        a.append(x)

a.sort()

for j in a:
    for k in range(b[j]):
        sys.stdout.write(str(j)+'\n')



#### 정렬을 하지 않고 출력하는법 ####
# 정렬하는 것과 시간차이가 클 것으로 예상했으나
# 생각보다 큰 차이가 나지는 않는다.

# import sys
# b = [0] * 10001
#
# for i in range(int(sys.stdin.readline())):
#     b[int(sys.stdin.readline())] += 1
#
# for i in range(10001):
#     if b[i] > 0:
#         for j in range(b[i]):
#             print(i)