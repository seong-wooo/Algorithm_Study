# n=1 부터 차근차근 확인을 해보니 피보나치 수열임을 알 수 있었다.
# 피보나치 수열만 작성하였을때 시간 초과가 났었다.
# 이는 너무 큰 수의 계산이었기 때문이었는데
# 이를 해결하기 위해서 15746의 나머지를 미리 구하여
# 작은 숫자의 형태로 계산을 진행하였다.


import sys

def fibo(n):
    prev = 1
    current = 1
    for i in range(2, n + 1):
        current , prev = (current+prev)%15746 ,current

    return current




n = int(sys.stdin.readline())

print(fibo(n) % 15746)