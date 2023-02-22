n, k = map(int, input().split())

count = 0
while  bin(n).count('1') > k:
    plus = 2 ** (bin(n)[::-1].index('1'))
    count += plus
    n += plus

print(count)

