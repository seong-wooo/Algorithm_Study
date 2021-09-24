# itertools 라이브러리의 permutations를 이용하여 구현하였다.
# 라이브러리를 잘 활용하자


from itertools import permutations

import sys

n, m = map(int, sys.stdin.readline().split())

permutations_list = [i for i in range(1,n+1)]

permutations_list = list(permutations(permutations_list, m))

for i in permutations_list:
    for j in i:
        print(j, end=" ")
    print()


# 리스트를 만들지 않고 permutation에 바로 대입을 하는 경우 훨씬 빠르게 동작한다.


# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)  # iter(tuple)
# for i in P:
#     print(' '.join(map(str, i)))