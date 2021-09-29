#왕실의 나이트
#내가 푼 풀이
#위,아래,좌,우와의 거리를 계산하고
#각 값을 리스트에 삽입한 뒤 정렬한다.
# [0][1] 인덱스의 값만 확인한다.
# 0 0-> 2 / 0 1->3 / 0 2이상->4
# 1 1 -> 4 / 1 2이상 -> 6
# 2 이상 -> 8

loc = input()

uplr = []
uplr.append(abs(int(loc[1]) - 1))
uplr.append(abs(int(loc[1]) - 8))
uplr.append(abs(ord(loc[0]) - ord('a')))
uplr.append(abs(ord(loc[0]) - ord('h')))


uplr.sort()

if uplr[0] == 0:
  if uplr[1] >= 2:
    print(4)
  else:
    print(2+uplr[1])

elif uplr[0] == 1:
  if uplr[1] >= 2:
    print(6)
  else:
    print(4)
else:
  print(8)



### 이동 방향을 정의하고 구현하기
# 경우의 수를 모두 적고 각 경우를 만족하는지의 여부를 따지기

input_data =input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

count = 0

for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if 1<=next_row<=8 and 1<=next_column<=8:
    count +=1

print(count)
