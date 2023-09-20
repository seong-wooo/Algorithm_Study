# 정렬 후 정렬 리스트와 원래 리스트사이를 연결할 때 어려움을겪었다.
# 접근시간을 빠르게 하기 위해 dictionary 를 사용하였다.


import sys

n = int(sys.stdin.readline())

x_list = list(map(int, sys.stdin.readline().split()))
x_list_sort = list(set(x_list))
x_list_sort.sort()

b= {}

for i in range(len(x_list_sort)):
    b[x_list_sort[i]] = i

for j in x_list:
    print(b[j], end=" ")


# 코드 수정

# for i in range(len(x_list_sort)):
#     b[x_list_sort[i]] = i
# for j in x_list:
#     print(b[j], end=" ")

# 이 부분을 다음과 같이 바꾼다
# 같은 코드지만 좀 더 간결하게 쓸 수 있다.

# b = {x_list_sort[i]:i for i in range(len(x_list_sort))}
# print(*[b[j] for j in x_list])
