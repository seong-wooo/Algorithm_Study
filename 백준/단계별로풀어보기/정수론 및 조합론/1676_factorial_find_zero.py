# 처음에는 그냥 무작정 factorial 계산을 하고
# 뒤에서 부터 0의 개수를 셌다.

import sys
from math import factorial

n = int(sys.stdin.readline())

n = str(factorial(n))


count = 0

for i in range(len(n)-1, -1, -1):
    if n[i] == "0":
        count += 1
    else:
        break

print(count)


# 위의 코드보다 간결하게 작성하여 보자
# factorial 문제라고 마냥 다 계산해버리면 오래걸릴 수도 있다.
# 숫자 뒤에 0이 나온다는 것은?
# 10의 배수라는 것이다
# 그렇다면 10이 나오기 위해서는 ?
# 10의 약수인 2,5가 존재해야한다.
# 5의 배수가 존재한다면 2의 배수는 당연하게 존재할 것이다, ( 5 > 2 )
# 따라서 5가 몇 번 들어가는지 구하면 된다

# n = int(sys.stdin.readline())
#
# count = 1
# total = 0
#
# while n >= 5**count:
#     total += n//(5**count)
#     count += 1
#
# print(total)


