from collections import deque
import sys

stack = deque()

for i in range(int(sys.stdin.readline())):
    instruction = sys.stdin.readline().strip()

    if "push" in instruction:
        stack.append(instruction.split()[1])
        continue

    if instruction == "pop":
        if not stack:
            print("-1")
            continue
        print(stack.pop())
        continue

    if instruction == "size":
        print(len(stack))
        continue

    if instruction == "empty":
        if stack:
            print("0")
            continue
        print("1")
        continue

    if instruction == "top":
        if stack:
            print(stack[-1])
            continue
        print("-1")

