import sys
from collections import deque

message1 = deque(sys.stdin.readline().rstrip())
message2 = deque()

for i in range(int(sys.stdin.readline())):
    instruction = sys.stdin.readline().strip()

    if "L" == instruction and message1:
        message2.append(message1.pop())

    elif "D" == instruction and message2:
        message1.append(message2.pop())

    elif "B" == instruction and message1:
        message1.pop()

    elif "P" in instruction:
        message1.append(instruction.split()[1])


print("".join(message1) + "".join(reversed(message2)))

