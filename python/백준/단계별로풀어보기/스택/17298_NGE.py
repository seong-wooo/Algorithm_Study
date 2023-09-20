# 스택을 이용하였다.
# stack에 기존 수열의 값과 인덱스를 함께 append 하여
# 특정 값에 해당하는 인덱스 정보를 쉽게 찾을 수 있었다.

import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = deque()
print_stack = [-1] * n

for i in range(n):
    if len(stack) == 0:
        stack.append((a[i],i))
    else:
        while len(stack) !=0 and stack[-1][0] < a[i]:
            print_stack[stack.pop()[1]] = a[i]

        stack.append((a[i],i))

for j in range(len(stack)):
    remainder = stack.pop()
    print_stack[remainder[1]] = -1

print(" ".join(map(str, print_stack)))

# 수정사항
# for j in range(len(stack)):
#     remainder = stack.pop()
#     print_stack[remainder[1]] = -1
# 이 부분은 굳이 쓰지않아도 됐었다.
# 어차피 print_stack에는 -1 값이 들어있었기 때문이다.
