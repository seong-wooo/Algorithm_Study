from collections import defaultdict

def solution(genres, plays):
    count = defaultdict(int)
    index = defaultdict(list)
    
    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        index[genres[i]].append([i, plays[i]])
    
    answer = []
    for g in sorted(count, key=lambda x: -count[x]):
        answer += [x[0] for x in sorted(index[g], key=lambda x: -x[1])[:2]]
    
    return answer
        