from collections import deque
def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0

    for city in map(lambda x: x.lower(), cities):
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
            
        cache.append(city)
        answer += 5
    return answer