# 1
# 2 4 8 6
# 3 9 7 1
# 4 6
# 5
# 6
# 7 9 3 1
# 8 4 2 6
# 9 1

# 1의 자리의 숫자만 본다
# 0의 제곱은 나올 수 없으므로 그 부분을 조심한다.

import sys

a= [1,5,6]
b= [2,3,7,8]
c= [4,9]
d =[0]

for i in range(int(sys.stdin.readline())):
    x,y = map(int, sys.stdin.readline().split())
    x %= 10

    if x in a:
        print(x)
    elif x in b:
        y = y%4 + 4

        print(pow(x,y)%10)
    elif x in c:
        y = y%2 + 2
        print(pow(x,y)%10)
    else:
        print(10)