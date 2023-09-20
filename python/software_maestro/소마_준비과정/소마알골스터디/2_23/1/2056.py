import sys
import heapq

input = sys.stdin.readline

n = int(input())
time = [0] * (n + 1)
indegree = [0] * (n + 1)
relation =[[] for _ in range(n + 1)]

for i in range(1, n + 1):
    t, ind, *nums = map(int, input().split())
    time[i] = t
    indegree[i] = ind
    for num in nums:
        relation[num].append(i)

q = [] #(걸리는 시간, 번호)
for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, [time[i], i])

total_time = 0
while q:
    t, num = heapq.heappop(q)
    for time_num in q:
        time_num[0] -= t

    total_time += t

    for next in relation[num]:
        indegree[next] -= 1
        if not indegree[next]:
            heapq.heappush(q, [time[next], next])

print(total_time)
