def solution(n, words):
    w = set()
    w.add(words[0])
    
    for i in range(1, len(words)):
        if words[i] in w or words[i-1][-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        w.add(words[i])
        
    return [0, 0]