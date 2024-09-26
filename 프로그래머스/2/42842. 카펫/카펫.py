def solution(brown, yellow):
    s = set(i for i in range(1, int(yellow ** 0.5) + 1) if yellow % i == 0)


    for n in s:
        if (n+2) * 2 + yellow // n * 2 == brown:
            return [yellow // n + 2, n+2]
    