import math

n, m = map(int, input().split())

# n개의 소시지, m명의 사람
print(m - math.gcd(n,m))