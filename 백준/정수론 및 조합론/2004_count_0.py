# 끝자리 0이 있다 = 10이 있다 = 2 * 5 가 있다
# 2의 개수와 5의 개수를 둘 다 구한후 작은 값이 답
# 처음 쓴 코드는 너무 복잡하다 함수를 이용해서 간단하게 나타내본다.
# count_num이라는 함수를 만들었다.
# factorial 안에 num 이 몇번 들어가는 지 구하는 함수이다.
# 예를 들어 25! 안에는  5, 10, 15, 20, 25 안에 총 6개의 5가 있다.


import sys

def count_num(n, num):
    i = 1
    count = 0
    while n >= pow(num, i):
        count += n // pow(num, i)
        i += 1
    return count

n, m = map(int, sys.stdin.readline().split())

count_2 = 0
count_5 = 0


count_2 = count_num(n,2) - count_num(m,2) - count_num(n-m,2)
count_5 = count_num(n,5) - count_num(m,5) - count_num(n-m,5)

print(min(count_2, count_5))