# 파이썬은 stack 구조를 제공하지 않는다
# pop을 자주 하는 문제이므로 더블 링크드 리스트로 구현된 deque 자료구조를 이용하여 구현하였다.
# 문제를 제출하였을 때 런타임 에러가 났는데
# 이를 해결하기 위해 sys를 import 하여 sys.stdin.readline()을 통해 입력을 받았다.
# 문제는 기본적인 stack을 구현하는 것이므로 stack의 기본 특성을 알고있었기에 어렵지 않았다.

from collections import deque
import sys

class Stack:
    def __init__(self):
        self.stack = deque()

    def stack_function(self, instruction):
        if "push" in instruction:
            self.stack.append(instruction.split()[1])

        elif instruction == "pop":
            if len(self.stack) == 0:
                return print(-1)
            else:
                return print(self.stack.pop())

        elif instruction == "size":
            return print(len(self.stack))

        elif instruction == "empty":
            if len(self.stack) == 0:
                return print(1)
            else:
                return print(0)

        elif instruction == "top":
            if len(self.stack) == 0:
                return print(-1)
            return print(self.stack[-1])

stack_test = Stack()

for i in range(int(sys.stdin.readline())):
    stack_test.stack_function(sys.stdin.readline().strip())

