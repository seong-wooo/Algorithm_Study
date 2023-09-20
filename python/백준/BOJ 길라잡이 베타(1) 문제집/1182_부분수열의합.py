# dfs를 이용한 재귀적인 풀이방법으로 풀었을 때
# 오류가 발생했는데 아직 이 오류의 해결 방법을 찾지 못하였다.
# 따라서 조합을 이용한 풀이로 변경하였다.
# 특정 부분 집합을 뽑는 경우 조합을 사용하면 편하다.

from itertools import combinations

n, s= map(int,input().split())

arr = list(map(int,input().split()))
count = 0
for i in range(1,n+1):
    com_list = list(combinations(arr,i))

    for com in com_list:
        if sum(com) == s:
            count += 1
print(count)


# def dfs(index, result):
#     if index == n-1:
#         count = 0
#         if s == result:
#             count += 1
#         elif s == result + arr[index]:
#             count+= 1
#         return count
#
#
#     return dfs(index+1, result + arr[index]) + dfs(index+1, result)
#
#
# print(dfs(0,0) if s!= 0 else dfs(0,0) -1)
#






