from collections import deque

sticks = input()
stack = deque()

total = 0
for i in range(len(sticks)):
    if sticks[i] == "(":
        stack.append("(")

    else:
        stack.pop()
        if sticks[i - 1] == "(":
            total += len(stack)
        else:
            total += 1
print(total)
