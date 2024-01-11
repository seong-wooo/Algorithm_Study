def solution(friends, gifts):
    d = {f: i for i, f in enumerate(friends)}
    graph = [[0] * (len(friends) + 1) for _ in range(len(friends))]
    
    for gift in gifts:
        a, b = map(lambda x : d[x], gift.split())
        graph[a][b] += 1
        graph[a][-1] += 1
        graph[b][-1] -= 1
    
    
    result = 0
    for j in range(len(graph)):
        present = 0
        for i in range(len(graph)):
            if graph[j][i] > graph[i][j]:
                present += 1
            elif graph[j][i] == graph[i][j] and graph[j][-1] > graph[i][-1]:
                present += 1
        result = max(result, present)
    return result
    
        
        
    