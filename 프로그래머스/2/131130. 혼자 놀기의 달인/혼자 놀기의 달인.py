def solution(cards):
    cards = [0] + cards
    visited = [False] * len(cards)
    
    i = 1
    groups = []
    while i < len(cards):
        if not visited[i]:
            visited[i] = True
            group = 1
            j = i
            while not visited[cards[j]]:
                visited[cards[j]] = True
                group += 1
                j = cards[j]
            groups.append(group)
        i += 1
    
    if len(groups) < 2:
        return 0 
    else:
        groups.sort()
        return groups[-1] * groups[-2]