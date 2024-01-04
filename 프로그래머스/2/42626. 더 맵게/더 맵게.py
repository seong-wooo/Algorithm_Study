from heapq import heappop, heappush, heapify
def solution(s, k):
    heapify(s)
    answer = 0
    while s[0] < k:
        s1 = heappop(s)
        if not s:
            return -1
        s2 = heappop(s)
        heappush(s, s1 + s2 * 2)
        answer += 1
    return answer