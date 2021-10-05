#이진 탐색 구현(재귀)

def binary_search(array,target,start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] < target:
    return binary_search(array,target,mid+1,end)
  else:
    return binary_search(array,target,start,mid-1)


array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search(array,11,0,len(array)-1)
if result == None:
    print("없음")
else:
    print(result + 1)