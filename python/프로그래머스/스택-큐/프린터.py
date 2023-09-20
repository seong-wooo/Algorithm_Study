# 나의 풀이 -> 무난
from collections import deque

def solution(priorities, location):

    printer = deque(priorities)

    answer = 1
    while printer:

        if printer[0] == max(printer):
            if location == 0:
                return answer
            else:
                printer.popleft()
                location -= 1
                answer += 1
        else:
            printer.append(printer.popleft())
            location -= 1


        if location < 0:
            location = len(printer) - 1