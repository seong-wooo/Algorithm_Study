import sys
from collections import deque


def change(tu):
    if tu[0] == 0:
        return str(tu[2])
    return ""

a, b, c = map(int, sys.stdin.readline().split())

q = deque()
result = set()
q.append((0, 0, c))
result.add((0, 0, c))

combinations = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
maximum = [a, b, c]

while q:
    bottles = q.popleft()

    for c in combinations:
        w_index, t_index = c[0], c[1]

        if bottles[w_index] > maximum[t_index] - bottles[t_index]:
            bottle_w = bottles[w_index] - (maximum[t_index] - bottles[t_index])
            bottle_t = maximum[t_index]


        else:
            bottle_t = bottles[t_index] +  bottles[w_index]
            bottle_w = 0

        new_bottles = [0] * 3
        new_bottles[w_index], new_bottles[t_index], new_bottles[3 - w_index - t_index] = bottle_w, bottle_t, bottles[
            3 - w_index - t_index]

        new_bottles = tuple(new_bottles)
        if new_bottles not in result:
            result.add(new_bottles)
            q.append(new_bottles)

real_result = set()
for r in result:
    if not r[0]:
        real_result.add(r[2])

print(*sorted(real_result))