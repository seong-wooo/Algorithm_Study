def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    win_nums = set( win_nums)
    min_count = 0
    zero_count = 0
    for num in lottos:
        if num == 0:
            zero_count += 1
        elif num in win_nums:
            min_count += 1

    max_count = min_count + zero_count

    if max_count >= 6:
        return [1,rank[min_count]]
    else:
        return [rank[max_count],rank[min_count]]


# 더 나은 풀이
# 훨씬 깔끔함
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]