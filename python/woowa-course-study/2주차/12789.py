from collections import deque

n = input()

line = deque(map(int, input().split()))

seq = 1

stack = deque()

while line:
    if line[0] == seq:
        line.popleft()
        seq += 1

    elif stack and stack[-1] == seq:
        stack.pop()
        seq += 1

    else:
        stack.append(line.popleft())

while stack:
    space_top = stack[-1]
    if space_top == seq:
        stack.pop()
        seq += 1
    else:
        break

if not stack:
    print("Nice")
else:
    print("Sad")
