import sys

n = int(sys.stdin.readline())
schedule = []
for i in range(n):
    schedule.append(list(map(int,sys.stdin.readline().split())))
# 끝나는 시간에 대하여 정렬을 하는 것은 알고있었다.
# 시작 시간에 대해서도 정렬을 해줘야 하는 이유:
# 만약 끝나는 시간에 대해서만 정렬했을 때
# [1,2],[5,5],[4,5] 로 정렬됐다면
# 들을 수 있는 수업은 2개
# 그러나 시작시간에 대해서도 정렬을 한다면
# [1,2],[4,5],[5,5] 들을 수 있는 수업은 3개

schedule.sort(key= lambda x:(x[1],x[0]))

i = 0
j = 1
count = 1
while j < n:
   if schedule[i][1] > schedule[j][0]:
       j += 1
   else:
       count += 1
       i = j
       j += 1

print(count)