from itertools import combinations

nan = [int(input()) for i in range(9)]

find = sum(nan) - 100

nan_com = list(combinations(nan, 2))

for nans in nan_com:
    if sum(nans) == find:
        for n in sorted(nan):
            if n not in nans:
                print(n)
        break