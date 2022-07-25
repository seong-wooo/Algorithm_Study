import sys
from collections import deque

n = int(sys.stdin.readline())

result = [int(sys.stdin.readline()) for _ in range(n)]

seq = sorted(result)

stack = deque()

index = 0

print_result = []

for x in seq:
    stack.append(x)
    print_result.append("+")

    while stack:
        if stack[-1] == result[index]:
            stack.pop()
            print_result.append("-")
            index += 1
        elif stack[-1] > result[index]:
            print("NO")
            sys.exit()
        else:
            break

print("\n".join(print_result))