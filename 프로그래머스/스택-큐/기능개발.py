from collections import deque


def solution(progresses, speeds):
    queue = deque(progresses)
    speeds = deque(speeds)
    result = []
    while queue:
        for i in range(len(queue)):
            queue[i] += speeds[i]

        elelment = 0
        while queue and queue[0] >= 100:
            queue.popleft()
            speeds.popleft()
            elelment += 1
        if elelment > 0:
            result.append(elelment)

    return result