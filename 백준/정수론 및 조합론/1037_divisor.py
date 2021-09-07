# 약수 중 (제일 큰값) * (제일 작은 값) = 구하고자 하는 수


#처음 쓴 코드
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
print(a[0] * a[-1])

#굳이 정렬을 하지 않고 제일 큰값과 작은 값만 찾으면된다
#수정된 코드

# a.sort()
# print(a[0] * a[-1])

#print(max(a) * min(a))