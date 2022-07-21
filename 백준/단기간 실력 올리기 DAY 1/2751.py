import sys

result = set(int(sys.stdin.readline()) for x in range(int(sys.stdin.readline())))

print("\n".join([str(i) for i in range(-1000000, 1000001) if i in result]))