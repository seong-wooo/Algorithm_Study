from itertools import combinations

n, m = map(int, input().split())

for j in list(combinations([i for i in range(1,n+1)], m)):
    print(*j)




print(*(1, 2, 3, 4, 5))