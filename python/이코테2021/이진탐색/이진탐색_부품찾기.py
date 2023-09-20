import sys

def binary_search(array, start,end, target):
  if start > end:
    return False
  
  mid = (start + end) // 2

  if array[mid] == target:
    return True
  elif array[mid] > target:
    return binary_search(array, start, mid-1, target)
  else:
    return binary_search(array, mid+1, end, target)



n = int(sys.stdin.readline())

store = list(map(int, sys.stdin.readline().split() ))

m = int(sys.stdin.readline())
custom = list(map(int,sys.stdin.readline().split() ))
store.sort()



for i in range(m):
  target = custom[i]
  if binary_search(store,0,n-1,target):
    print("yes", end=" ")
  else:
    print("no", end= " ")








# 이 문제는 사실 set( ) 자료형으로 구현해도 된다.
# 단순히 특정 데이터가 존재하는지 검사만 하면 되니까 

# n = int(input()
# array = set(map(int,input().split()))
# m = int(input())
# x = list(map(int,input().split()))

# for i in x:
#	if i in array:
#		print('yes', end= " ")
#	else:
#		print('no', end = " ")
  