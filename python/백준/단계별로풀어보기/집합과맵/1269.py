import sys

n, m = map(int, sys.stdin.readline().split())

print(n+m - len(set(sys.stdin.readline().split()) & set(sys.stdin.readline().split())) * 2)

