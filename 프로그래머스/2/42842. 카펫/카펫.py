def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0 and 2 * i + 2 * (yellow // i) + 4 == brown:
            return [yellow // i + 2, i + 2]
    return []
    
        