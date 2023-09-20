import sys

n, m = map(int, sys.stdin.readline().split())
he = set(sys.stdin.readline() for _ in range(n))
se = set(sys.stdin.readline() for _ in range(m))
he_se = sorted(list(he & se))
print(len(he_se))
print("".join(he_se))