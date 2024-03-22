from collections import deque

def solution(cacheSize, cities):
    q = deque(maxlen = cacheSize)
    
    answer = 0

    for city in cities:
        city = city.lower()
        index = findIndex(q, city)
        if index == -1:
            answer += 5
        else:
            answer += 1
            del q[index]
        q.append(city)
    
    return answer

def findIndex(q, city):
    
    for i in range(len(q)):
        if q[i] == city:
            return i
    return -1
    