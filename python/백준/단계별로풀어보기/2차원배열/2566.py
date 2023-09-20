import sys

rowcol = sum([list(map(int, sys.stdin.readline().split())) for _ in range(9)], [])

maximum = max(rowcol)
maximum_index = rowcol.index(maximum)

print(maximum)
print(maximum_index // 9 + 1, maximum_index % 9 + 1)