# 오늘 공부한 heapq를 바로 응용해보았다.
# 리스트를 받아서 우선순위큐로 만들고
# 최솟값이 k보다 작고 길이가 1보다 크다면
# heappop과 heappush를 이용하여 mix한다.


import heapq

def solution(scoville, k):
    heapq.heapify(scoville)

    mix = 0
    while scoville[0] < k and len(scoville) > 1: # 여기서 scoville의 길이를 계속 측정해야함
                                                 # size 변수를 만들어서 size의 크기를 조절하자.
        sc = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, sc)
        mix += 1

    if heapq.heappop(scoville) >= k:
        return mix
    return -1

# 시간을 더 줄여보자
# heappushpop 함수를 사용한다
# heappushpop(list, x) 는 list에 x를 삽입하고 가장 작은 원소를 pop하며 return 한다.
# heappush와 heappop을 둘 다 쓰는 것 보다 효율적이다.

# import heapq
#
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     size, cnt = len(scoville) - 1, 0
#     f = heapq.heappop(scoville)
#     while size > 0:
#         s = heapq.heappop(scoville)
#         f = heapq.heappushpop(scoville, f + s + s)
#         if f >= K:
#             return cnt + 1
#         cnt += 1
#         size -= 1
#     return -1