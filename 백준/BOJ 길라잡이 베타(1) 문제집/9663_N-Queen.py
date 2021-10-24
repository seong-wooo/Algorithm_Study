# pypy로 23176ms나 걸리는 코드
# 엄청 오래걸린다.
# n개의 줄에 n개의 퀸이 들어가야하므로 모든 줄에 1개씩 퀸이 들어가야한다.
# 1라인씩 차근차근 경우의 수를 따지는 알고리즘이다.

n = int(input())

def dfs(arr):

  not_x_list =set(arr)

  for i in range(1, len(arr)+1):
    not_x_list.add(arr[-i]-i) 
    not_x_list.add(arr[-i]+i)

  x_list = [i for i in range(1,n+1) if i not in not_x_list]

  if len(arr) == n-1:
    return len(x_list)
  count = 0
  for x in x_list:
    count += dfs(arr + [x])
  return count

print(dfs([]))

