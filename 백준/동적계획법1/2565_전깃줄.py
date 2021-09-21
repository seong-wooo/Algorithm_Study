# 11053과 거의 유사한 문제
# a,b 를 a에 대하여 정렬 후
# b에 대해서 가장 증가하는 부분 수열을 구한다.
# 총 길이 - 가장 증가하는 부분 수열의 크기 = 잘라야 할 전깃줄의 개수
import sys

n = int(sys.stdin.readline())

ab =[]
for i in range(n):
    ab.append(list(map(int, sys.stdin.readline().split())))

ab.sort(key=lambda x:x[0])

asc_seq = [1]

for i in range(1, n):
    asc = 1
    for j in range(i-1, -1 , -1):
        if ab[i][1] > ab[j][1]:
            asc = max(asc, asc_seq[j] + 1)

    asc_seq.append(asc)

print(n-max(asc_seq))
