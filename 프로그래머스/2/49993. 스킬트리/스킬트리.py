def solution(skill, skill_trees):
    
    orders = dict()
    
    for i, s in enumerate(skill):
        orders[s] = i
    
    link = dict()
    
    for i in range(len(skill)):
        link[skill[i]] = list(skill[i+1:])

    result = 0
    for tree in skill_trees:
        t = dict(orders)
        if can(t, tree, link):
            result += 1
    return result    
                    
def can(t, tree, link):
    for a in tree:
        if a in t:
            if t[a] >= 1:
                return False

            for l in link[a]:
                t[l] -= 1
    return True