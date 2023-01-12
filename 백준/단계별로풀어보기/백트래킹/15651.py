from itertools import product

n, m = map(int, input().split())


print("\n".join(list(map(" ".join, product([str(i) for i in range(1, n + 1)], repeat = m)))))