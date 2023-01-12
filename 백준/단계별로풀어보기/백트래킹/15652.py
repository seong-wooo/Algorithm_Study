from itertools import combinations_with_replacement

n, m = map(int, input().split())

print("\n".join(map(" ".join, combinations_with_replacement([str(i) for i in range(1, n+1)], m))))
