n, k = map(int, input().split())

count = 0
while bin(n).count("1") > k:
    buy = 2 ** bin(n)[::-1].index("1")
    count += buy
    n += buy

print(count)