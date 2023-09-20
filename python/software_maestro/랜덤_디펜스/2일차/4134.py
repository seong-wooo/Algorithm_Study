import sys

input = sys.stdin.readline

ns = [int(input()) for _ in range(int(input()))]


def isPrime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


for n in ns:
    if n <= 2:
        print(2)
        continue

    a = n
    while not isPrime(a):
        a += 1

    print(a)


# 소수 판별
# 1. 제곱근 이용해서 빠르게 소수 여부 판별하기
# 2. 에라토네스체 : 소수 판별해야 되는 값의 범위가 크고, 값 자체는 작을 때