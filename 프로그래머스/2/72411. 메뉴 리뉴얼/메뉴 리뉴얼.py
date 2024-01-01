from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    d = [defaultdict(int) for _ in range(len(course))]
    
    for order in orders:
        for i in range(len(course)):
            for comb in combinations(order, course[i]):
                d[i]["".join(sorted(comb))] += 1
    
    answer = []
    for menu in d: 
        answer += find_max(menu)

    return sorted(answer)


def find_max(menu):
    if not menu:
        return []
    m = max(menu, key = lambda x : menu[x])
    
    if menu[m] < 2:
        return []
    
    print(menu)
    return [k for k in menu if menu[k] == menu[m]]