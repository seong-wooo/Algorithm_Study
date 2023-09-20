# 리스트를 이용하여 정렬한다.
# 파이썬의 기본 정렬 알고리즘은 시간 복잡도가 O(n)이다.
# 따라서 기본 정렬을 사용했고 시간 절약을 위해 sys.stdin.readline()을 사용했다.
# sys.stdout.write() print() 의 차이: 전자는 끝에 \n이 없고 후자는 있다.


import sys

a = []
for i in range(int(sys.stdin.readline())):
    a.append(int(sys.stdin.readline()))
a.sort()

for j in a:
    sys.stdout.write(str(j)+'\n')