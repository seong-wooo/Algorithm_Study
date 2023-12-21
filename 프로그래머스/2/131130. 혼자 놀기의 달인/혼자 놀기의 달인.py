def solution(cards):
    visited = [False] * len(cards)
    groups = []
    
    
    for i in range(len(visited)):
        if not visited[i]:
            group = 0
            j = i
            while not visited[j]:
                group += 1
                visited[j] = True
                j = cards[j] - 1
            groups.append(group)
    
    if len(groups) == 1:
        return 0
    
    groups.sort(reverse = True)
    
    return groups[0] * groups[1]

    