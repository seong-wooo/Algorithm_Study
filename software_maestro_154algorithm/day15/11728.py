import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split() + input().split()))

print(*sorted(a))