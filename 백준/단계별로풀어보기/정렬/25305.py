import sys

n, k = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))
students.sort(reverse=True)

print(students[k-1])
