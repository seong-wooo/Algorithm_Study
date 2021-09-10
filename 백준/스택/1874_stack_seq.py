# 기본 스택의 성질을 이용한다
# 제공된 수열의 각 항을 순서대로 방문한다
# 방문한 항의 값이 이때까지 방문한 숫자의 최대 크다면
# max(방문한 숫자)+1 부터 현재 방문한 항의 값까지 push한다
# 방문한 항의 값이 이때까지 방문한 숫자의 최대보다 작다면 pop한다
# 이때 pop한 숫자가 방문한 항의 값과 다르면 NO를 출력한다.

import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
seq = []
for i in range(n):
    seq.append(int(sys.stdin.readline()))

top = 0
print_list = []
for i in range(len(seq)):
    if seq[i] > top:
        for j in range(top + 1, seq[i]+1):
            stack.append(j)
            print_list.append("+")
        top = stack.pop()
        print_list.append("-")
    else:
        if stack.pop() != seq[i]:
            print("NO")
            exit()
        else:
            print_list.append("-")

for i in print_list:
    print(i, end=" ")