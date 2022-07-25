import sys

result = sorted(list(set(sys.stdin.readline().rstrip() for i in range(int(input())))), key=lambda x: (len(x), x))

print("\n".join(result))
