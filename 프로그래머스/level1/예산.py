# 정렬 후 작은거부터 뺴주기
# 그리디
def solution(budget, d):
    budget.sort()
    count = 0
    for i in range(len(budget)):
        if d >= budget[i]:
            d -= budget[i]
            count += 1
        else:
            break
    return count