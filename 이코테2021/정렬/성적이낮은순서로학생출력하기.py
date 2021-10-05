#성적이 낮은 순서로 학생 출력하기

n = int(input())
array=[]
for i in range(n):
  array.append(input().split())

array.sort(key=lambda x:x[1])

for i in array:
  print(i[0], end= " ")
  