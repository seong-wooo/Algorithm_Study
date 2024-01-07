def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    q = []
    qSize = 0
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.pop(q.index(city))
            q.append(city)
    
        else:
            answer += 5        
            if qSize < cacheSize:
                q.append(city)
                qSize += 1
            else:
                q.pop(0)
                q.append(city)
                
    return answer