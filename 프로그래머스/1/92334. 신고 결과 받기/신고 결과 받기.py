from collections import defaultdict

def solution(id_list, report, k):
    
    d_id = defaultdict(set)
    d_report = defaultdict(int)
    
    for re in report:
        a, b = re.split()
        if b not in d_id[a]:
            d_id[a].add(b)
            d_report[b] += 1
    
    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        for j in d_id[id_list[i]]:
            if d_report[j] >= k:
                answer[i] += 1
                
    return answer