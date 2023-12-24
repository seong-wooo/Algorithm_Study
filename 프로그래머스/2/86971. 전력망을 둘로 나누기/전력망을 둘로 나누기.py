from collections import Counter
def solution(n, wires):
    result = n
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i + 1:]
        parent = [j for j in range(n + 1)]
        for cw in cut_wires:
            union(cw[0], cw[1], parent)
        
        for j in range(len(parent)):
            find_parent(j, parent)
        c = Counter(parent)
        
        result = min(result, 2*c.most_common()[0][1] - n)
    return result
        
        
def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)    
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
        
def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]