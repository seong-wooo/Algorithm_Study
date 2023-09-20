# 단순히 in 을 사용하니까 시간초과가 떴다
# 이진탐색을 구현하여 시간복잡도를 O(log n)으로 만들었다.
# 이진 탐색으로 구현했을 때 756ms
# 해쉬 함수로 구현했을 때 212ms
# 해쉬 함수로 구현하면 시간복잡도 O(1)으로 만들 수 있다.
import sys

def find_n(a, n,front,end):
    if front >= end:
        if a[front] == n :
            return 1
        else:
            return 0
    mid = (front + end) // 2

    if a[mid] == n:
        return 1
    elif a[mid] > n:
        return find_n(a, n, front, mid - 1)

    else:
        return find_n(a, n, mid + 1, end)



n = int(sys.stdin.readline())
a =list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in b:
    print(find_n(a, i,0,len(a)-1))

# 해쉬 함수로 구현했을 때 212ms
#####################################################
# n = int(sys.stdin.readline())
# a =set(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split()))
#
# for i in b:
#     if i in a:
#         print(1)
#     else:
#         print(0)